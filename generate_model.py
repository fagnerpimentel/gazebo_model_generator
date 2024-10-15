import os
import math
from jinja2 import Environment, FileSystemLoader

config_data = {
    "author_name": "Fagner Pimentel",  
    "author_email": "fagnerpimentel@gmail.com",
    "model_name": "k404",
    "model_description": "Sala 404 do prédio K do centro universitário FEI."
}
sdf_data = [
    {"x":0.75, "y":5.00, "z":0, "width":1.500, "depth": 0.015, "height": 0.35},
    {"x":0.00, "y":2.50, "z":0, "width":0.015, "depth": 5.000, "height": 0.35},
    {"x":0.75, "y":0.00, "z":0, "width":1.500, "depth": 0.015, "height": 0.35},
    {"x":1.50, "y":1.25, "z":0, "width":0.015, "depth": 2.500, "height": 0.35},
    {"x":1.90, "y":2.50, "z":0, "width":0.800, "depth": 0.015, "height": 0.35},
    {"x":2.30, "y":1.25, "z":0, "width":0.015, "depth": 2.500, "height": 0.35},
    {"x":3.15, "y":0.00, "z":0, "width":1.700, "depth": 0.015, "height": 0.35},
    {"x":4.00, "y":1.25, "z":0, "width":0.015, "depth": 2.500, "height": 0.35},
]

for i in range(290 - 1):
    x = 1.5 + 2.5 * math.sin(i/180)
    y = 2.5 + 2.5 * math.cos(i/180)
    sdf_data.append(
        {"x":x, "y":y, "z":0, "width":0.015, "depth": 0.015, "height": 0.35}
    )



path = "./"+config_data["model_name"]
file_config = path+"/model.config"
file_sdf = path+"/model.sdf"

environment = Environment(loader=FileSystemLoader("templates/"))
template_config = environment.get_template("model.config")
template_sdf = environment.get_template("model.sdf")

content_config = template_config.render(
    author_name=config_data["author_name"],
    author_email=config_data["author_email"],
    model_name=config_data["model_name"],
    model_description=config_data["model_description"]
)

content_sdf = template_sdf.render(model_name=config_data["model_name"], data_idx=zip(sdf_data, range(len(sdf_data))))

if(not os.path.exists(path)): 
   os.mkdir(path)

with open(file_config, mode="w", encoding="utf-8") as message:
    message.write(content_config)
    print(f"... wrote {file_config}")
with open(file_sdf, mode="w", encoding="utf-8") as message:
    message.write(content_sdf)
    print(f"... wrote {file_sdf}")