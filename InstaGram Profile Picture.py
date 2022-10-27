import os
import instaloader

def picture_download(username):
    parser=instaloader.Instaloader()
    #"Change Directory to Downloads"
    os.chdir(os.path.join(os.path.expanduser('~'),'Downloads'))
    #"Create custom folder"
    if os.path.isdir("d:/Notebook Ex/Python Codes/Insta Download"):
        os.chdir("d:/Notebook Ex/Python Codes/Insta Download")
        #"Download the data"
        return parser.download_profile(username,profile_pic_only=True)
    

if __name__ == "__main__":
    user=input("Enter Insta Account: ")
    picture_download(user)            
