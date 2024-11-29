import numpy as np
import utils

class tagger_node:
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("Caption",)
    FUNCTION = "create_caption"
    CATEGORY = "5x00/GPT4o"

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Image" : ("IMAGE", {}), 
                "Prompt" : ("STRING", {"multiline": True, "default": "Describe the image."}),
                "API_Key" : ("STRING", {}),
                "Service" : (["OpenAI", "Claude"],),
            },
        }

    def create_caption(self, Image, Prompt, API_Key, Service):
        print("Generating caption for the image...")
        caption = ""
        if Service == "OpenAI":
            caption = utils.gen_openai(API_Key, Image, Prompt)
        if Service == "Claude":
            caption = utils.gen_claude(API_Key, Image, Prompt)
        print(f"Caption generated: {caption}")
        return caption
    
NODE_CLASS_MAPPINGS = {
    "Image Tagger" : tagger_node,
}