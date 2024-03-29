import subprocess


# subprocess.call("apt update -qq", shell=True, stdout=None, stderr=None)
# subprocess.call("apt -y install -qq aria2", shell=True, stdout=None, stderr=None)
# subprocess.call(
#     "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://civitai.com/api/download/models/119057 -d /comfyui/models/checkpoints",
#     shell=True,
#     stdout=None,
#     stderr=None,
# )
# subprocess.call(
#     "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/h94/IP-Adapter/resolve/main/models/image_encoder/pytorch_model.bin -d /comfyui/models/clip_vision/SD1.5 -o pytorch_model.bin",
#     shell=True,
#     stdout=None,
#     stderr=None,
# )
# subprocess.call(
#     "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/gemasai/4x_NMKD-Superscale-SP_178000_G/resolve/main/4x_NMKD-Superscale-SP_178000_G.pth -d /comfyui/models/upscale_models -o 4x_NMKD-Superscale-SP_178000_G.pth",
#     shell=True,
#     stdout=None,
#     stderr=None,
# )
# subprocess.call(
#     "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/Acly/Omni-SR/resolve/main/OmniSR_X2_DIV2K.safetensors -d /comfyui/models/upscale_models -o OmniSR_X2_DIV2K.safetensors",
#     shell=True,
#     stdout=None,
#     stderr=None,
# )
# subprocess.call(
#     "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/Acly/Omni-SR/resolve/main/OmniSR_X3_DIV2K.safetensors -d /comfyui/models/upscale_models -o OmniSR_X3_DIV2K.safetensors",
#     shell=True,
#     stdout=None,
#     stderr=None,
# )
# subprocess.call(
#     "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/Acly/Omni-SR/resolve/main/OmniSR_X4_DIV2K.safetensors -d /comfyui/models/upscale_models -o OmniSR_X4_DIV2K.safetensors",
#     shell=True,
#     stdout=None,
#     stderr=None,
# )

# print('download end')


class Download:
    """
    A example node

    Class methods
    -------------
    INPUT_TYPES (dict):
        Tell the main program input parameters of nodes.

    Attributes
    ----------
    RETURN_TYPES (`tuple`):
        The type of each element in the output tulple.
    RETURN_NAMES (`tuple`):
        Optional: The name of each output in the output tulple.
    FUNCTION (`str`):
        The name of the entry-point method. For example, if `FUNCTION = "execute"` then it will run Example().execute()
    OUTPUT_NODE ([`bool`]):
        If this node is an output node that outputs a result/image from the graph. The SaveImage node is an example.
        The backend iterates on these output nodes and tries to execute all their parents if their parent graph is properly connected.
        Assumed to be False if not present.
    CATEGORY (`str`):
        The category the node should appear in the UI.
    execute(s) -> tuple || None:
        The entry point method. The name of this method must be the same as the value of property `FUNCTION`.
        For example, if `FUNCTION = "execute"` then this method's name must be `execute`, if `FUNCTION = "foo"` then it must be `foo`.
    """

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        """
        Return a dictionary which contains config for all input fields.
        Some types (string): "MODEL", "VAE", "CLIP", "CONDITIONING", "LATENT", "IMAGE", "INT", "STRING", "FLOAT".
        Input types "INT", "STRING" or "FLOAT" are special values for fields on the node.
        The type can be a list for selection.

        Returns: `dict`:
            - Key input_fields_group (`string`): Can be either required, hidden or optional. A node class must have property `required`
            - Value input_fields (`dict`): Contains input fields config:
                * Key field_name (`string`): Name of a entry-point method's argument
                * Value field_config (`tuple`):
                    + First value is a string indicate the type of field or a list for selection.
                    + Secound value is a config for type "INT", "STRING" or "FLOAT".
        """
        return {
            "required": {
                "string": (
                    "STRING",
                    {
                        "multiline": False,  # True if you want the field to look like the one on the ClipTextEncode node
                        "default": "1111",
                    },
                ),
            },
        }

    FUNCTION = "test"

    RETURN_TYPES = ()

    OUTPUT_NODE = True

    CATEGORY = "_for_testing"

    def test(self, string):
        if string:
            subprocess.call(string, shell=True, stdout=None, stderr=None)
        return {}


# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {"Download": Download}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {"Download": "Download Node"}
