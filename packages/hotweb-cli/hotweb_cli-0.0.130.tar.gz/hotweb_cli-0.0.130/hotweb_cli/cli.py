import argparse
import os
import subprocess
import json
# input wrapper
def Input(text,attempts = 3):
    while attempts >0:
        value = input(text)
        if len(value)==0:
            attempts -=1
            continue
        attempts = 0
        return value
# CREATE MODELS
# models __init__.py skeleton, from model_skeleton.py
def skeleton_template(args):
    os.chdir(os.path.join(os.getcwd(),"models"))
    filenamess = os.listdir()
    imports_ =""
    for file in filenamess:
        if file =="__init__.py":
            continue
        if file.endswith(".py"):
            val = f"from {file[:-3]} import {file[:-3].lower().capitalize()}"
            imports_ = imports_ + val + "\n" 
    temp=f"""
{imports_}
    """
    return temp
def run_app(app="app.py"):
    app = os.path.join(os.getcwd(),app)
    if os.path.exists(app):
        subprocess.run("python app.py")
    else:
        print("<--------------App not found in the current directory--------------->")
        # to raise error later versions
def model_func_generator(model,args):
    """
    teplate for creating models folder
    ---------------------------------------------------------------------------------
    import the db configs folder from the config.json
    """
    """with open("config.json","r") as f:
        config = json.load(f)"""
    model_kv =f"""
from hotweb.models.models import Models
from hotweb.models.models import DBConnection
import json
import os
with open("config.json","r") as f:
    config = json.load(f)
conn = DBConnection(config['dialect'],db_config=config)
if os.path.exists(os.path.join(os.getcwd(),'app.json')):
    with open('app.json','r') as f:
        data = json.load(f)
{model.lower().capitalize()} = Models('{model}',db=conn,dialect=config['dialect'])
{model.lower().capitalize()}.init('{model}',{
            args
            })
def {model}():
    {args}
    """
    return model_kv
def models(args):
    
    """
    check if the cwd has models folder, else create one
    """
    if not os.path.exists(os.path.join(os.getcwd(),"models")):
        os.mkdir("models")
        print("========just created models folder======")
    model_name = Input("Enter Model Name...").lower()
    models_ = {}
    while True:
        fields = Input("enter fields (fieldname:datatype)-->").lower()
        print(fields.split(":"))
        ask = input("enter more fields (yes/no)-->").lower()
        models_[fields.split(":")[0]] = str(fields.split(":")[1])
        if ask =="no" or ask=="n":
             # to update this
            break
    model_dir = os.path.join(os.getcwd(),"models",f"{model_name}.py")
    model_skeleton = os.path.join(os.getcwd(),"models","__init__.py")
    config_file = os.path.join(os.getcwd(),"models","config.json")
    with open(config_file,"w") as f:
        db_configs = {
            "host":"host_name_here",
            "port":"port",
            "username":"username",
            "password":"password",
            "database":"DB_NAME_HERE",
            "dialect":"mysql",
            "options":{}
        }
        json.dump(db_configs,f,indent=2)
    with open(model_dir,"w") as f:
        f.write(model_func_generator(model_name,models_))
    with open(model_skeleton,"w") as f:
        f.write(skeleton_template("nothing"))
# extract app name from libs/settings.py
def arg_handler_create_app(args):

    print(f"================CREATING {args.appname} App===================================")
    print(os.getcwd())
    curr = os.getcwd()
    # get file paths, joining
    static = os.path.join(curr,f"{args.appname}","libs","static")
    #app_config = os.path.join(curr,f"{args.appname}","libs")
    app_js = os.path.join(curr,f"{args.appname}","libs","static",f"{args.appname}","js")
    app_css = os.path.join(curr,f"{args.appname}","libs","static",f"{args.appname}","css")
    app_html = os.path.join(curr,f"{args.appname}","libs","static",f"{args.appname}","templates")
    os.mkdir(os.path.join(curr,f"{args.appname}"))
    dirs = [static,app_js,app_css,app_html]
    for dir_ in dirs:
        os.makedirs(dir_)
    # creating the files
    app_js_ = os.path.join(curr,f"{args.appname}","libs","static",f"{args.appname}","js",f"{args.appname}.js")
    app_css_ = os.path.join(curr,f"{args.appname}","libs","static",f"{args.appname}","css",f"{args.appname}.css")
    app_html_ = os.path.join(curr,f"{args.appname}","libs","static",f"{args.appname}","templates",f"{args.appname}.html")
    dirs = [app_js_,app_css_,app_html_]
    for dir_ in dirs:
        with open(dir_,"w") as f:
            f.write("")
    file_py = os.path.join(curr,f"{args.appname}","app.py")
    file_json = os.path.join(curr,f"{args.appname}","app.json")
    file_init = os.path.join(curr,f"{args.appname}","__init__.py")
    file_read = os.path.join(curr,f"{args.appname}","read_this_file_for_help.py")
    # libs/settings.py
    with open(os.path.join(curr,f"{args.appname}","libs","settings.py"),"w") as f:
        f.write(f"#test 123 \n {{args.appname}}")
    with open(file_py,"w") as f:
        f.write("#test 123")
    with open(file_json,"w") as f:
        f.write("{ \n }")
    with open(file_init,"w") as f:
        f.write(f"# ======================= {args.appname} App============================")
    with open(file_read,"w") as f:
        f.write(f"# ============READ THIS FILE TO GET MORE HELP ======================")
        
    print(f"================CREATED {args.appname} APP SUCCESSFULLY=======================")
def create_migration(args):
    curr = os.getcwd()
    
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("name")
    parser.add_argument("appname")

    args = parser.parse_args()
    # create the app
    if args.name.lower() == "create_app":
        arg_handler_create_app(args)
    elif args.name.lower() == "help":
        pass
    elif (args.name.lower() == "start" or args.name.lower() == "run" ) and args.appname.lower() =="server":
        run_app()
    elif args.name.lower() =="create" and args.appname.lower() =="migration":
        create_migration(args)
    elif args.name =="db:migrate":
        pass
    elif (args.name.lower() =="models" or args.name.lower() =="model") and args.appname.lower() =="init":
        model_func_generator("users",args)
    elif args.name.lower() =="model:generate":
        models(args)
        

    print(f"args === {args}, age==={args.name}")