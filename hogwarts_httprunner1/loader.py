import  yaml

def load_yaml(yaml_file):
    with open(yaml_file,"r",encoding='utf-8') as f:
        yml_contend = f.read()
        loaded_json = yaml.load(yml_contend)

    return loaded_json