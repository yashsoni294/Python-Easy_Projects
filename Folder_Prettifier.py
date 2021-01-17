import os
def soldier_prettify_my_folder(folder_path,file_name,file_format):
    os.chdir(folder_path)
    a=os.listdir(folder_path)
    for i in a:
        ab=os.path.isdir(i)
        if ab==True:
            os.rename(i,i.capitalize())
    n=1
    for thg in a:
        asdfcx=os.path.isfile(thg)
        if asdfcx==True:
            rer=thg.split(".")
            if rer[1]==file_format:
                os.rename(thg,f"{n}.{file_format}")
                n+=1
    for pak in a:
        if pak==file_name:
            with open(file_name,"r+") as qskfrc:
                qlxkf=qskfrc.readlines()
            with open(file_name,"w") as file:
                file.write("")
            with open(file_name, "a") as file:
                for yreow in qlxkf:
                    yreow = yreow.capitalize()
                    file.writelines(yreow)
folder=soldier_prettify_my_folder("G://bhaa photos/DCIM/camera","mahakalvijayam.txt","jpg")
