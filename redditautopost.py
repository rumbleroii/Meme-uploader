#Written by scoppy the lord



import instabot , os , praw , time , shutil , urllib.request , glob
from tqdm import tqdm
from redvid import Downloader

bot = instabot.Bot()

#user login instagram
try:
    bot.login(username = '     ' , password = '    ')
    print("Login Successfull")

except:
    print('Error during login')

path = 'C:/Users/mrith/OneDrive/Desktop/Instagram Bot Project/Main/amongus'

if os.path.exists('C:/Users/mrith/OneDrive/Desktop/Instagram Bot Project/Main/amongus'):

    print('Folder exists , deleting')
    shutil.rmtree('C:/Users/mrith/OneDrive/Desktop/Instagram Bot Project/Main/amongus')


print('Folder created')
os.mkdir(path)



#Reddit API
url = 'https://www.reddit.com/'
reddit = praw.Reddit(
                client_id='   ',
                client_secret='   ',
                password='    ',
                user_agent='    ',
                username='    '
            )

subreddit = reddit.subreddit('    ').search('flair:"Humor"' , sort = 'top' ,time_filter= 'day')

no_of_post = 0


for submission in subreddit:
    no_of_post += 1
    post_type = 'picture'

    if no_of_post == 51:
        break

    else:
        url = (submission.url)
        redditor_name = submission.author
        file_name = str(no_of_post)

        if url.endswith(".jpg"):
            file_name += ".jpg"
            found = True
                
        elif url.endswith(".png"):
            file_name += ".png"
            found = True
            
        else:
            continue
            found = True
            post_type = 'video'
            file_name+='_video.mp4'
            

        picture_path = ' '+ file_name

        if found == True:
            if post_type == 'video':

                try:
                    video_path = urllib.request.urlretrieve(url , picture_path)
                    print('Video Downloaded')
      

                except Exception as e:
                    print(e)
                    print('Error Uploading video file, continuing')
                    continue

                finally:
                    upload_status = bot.upload_video(picture_path , caption="""Follow for more memes \nBy: u/{}\n
                                                #love #TagsForLikes #TagsForLikesApp #TFLers #tweegram #photooftheday #20likes #amazing #meme #dankmemes #gamingmemes #memes #amongus #amongusmemes #amongusmemes #among""".format(redditor_name))
                        
                    if upload_status:
                        print(file_name + ' File Uploaded')
                    else:
                        continue
                    
                    
                
                

            else:
                try:
                    urllib.request.urlretrieve(url , picture_path)
                    print('picture saved')
                    upload_status = bot.upload_photo(' '+ file_name , caption="""Follow for more  memes \nBy: u/{}\n
                                            #love #TagsForLikes #TagsForLikesApp #TFLers #tweegram #photooftheday #20likes #amazing #meme #dankmemes #gamingmemes #memes #amongus #amongusmemes #amongusmemes #among""".format(redditor_name))

                    if upload_status:
                        print(file_name + ' File Uploaded')
                    else:
                        continue

                except Exception as e:
                    print(e)
                    print('Error Uploading picture file , continuing')
                    continue
        
                


                urllib.request.urlretrieve(url , picture_path)
                print('picture saved')

    print(file_name)
    print("Cooldown time {} min".format(30*60))
    for i in tqdm(range(30*60)):
        time.sleep(1)
    print('Next itertion')

else:
    print('Operation Over')



print('Error')
