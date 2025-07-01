import numpy as np
import cv2
from PIL import Image, ImageDraw, ImageFont
from .get_float_figure import get_figure, get_img
from .get_item_colors import get_colors


def generate_animation(ntables, tab_path, img_path, output_path):

    rating_range = (650,950)
    image_path = img_path + "{}.png"
    file_path = tab_path + "table_data_{}.txt"

    color_dict = get_colors(ntables, file_path)


    get_sz = get_img().size
    fps = 40
    output_video_path = output_path + 'cricket_rnk_bat_1990_2000.mp4'

    #Initialize OpenCV video writer 
    #fourcc = cv2.VideoWriter_fourcc(*'XVID')
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video_writer = cv2.VideoWriter(output_video_path, fourcc, fps, get_sz)

    #check1 ---> 5841
    #check2 ---> 6010

    #5841 --> 1990
    #9490 --> 1999

    logo_fr=0
    step = 15
    for onef in range(1,ntables-step,step):

        logo_fr += 1
        if (logo_fr % 3)==0: 
            animate_logo = True
        else:
            animate_logo = False
        
        DefImg=["item", "item", "item"]
    
        file_path_cr = file_path.format(onef)
        file_path_nxt = file_path.format(onef+step)

        day_cr=[]
        month_cr=[]
        year_cr=[]
        name_cr=[]
        rank_cr=[]
        rating_cr=[]
        ln_cr=[]

        day_nxt=[]
        month_nxt=[]
        year_nxt=[]
        name_nxt=[]
        rank_nxt=[]
        rating_nxt=[]
        ln_nxt=[]

        cr= open(file_path_cr,"r")
        lines_cr = cr.readlines()
        count_cr =0
        for x in lines_cr:
            count_cr += 1
            ln_cr.append(count_cr)
            day_cr.append(x.split('\t')[0])
            month_cr.append(x.split('\t')[1])
            year_cr.append(x.split('\t')[2])
            name_cr.append(x.split("\t")[5])
            rating_cr.append(x.split("\t")[4])
            rank_cr.append(x.split("\t")[3])

        cr.close()

        nxt = open(file_path_nxt,"r")
        lines_nxt = nxt.readlines()
        count_nxt =0
    
        for x in lines_nxt:
            count_nxt += 1
            ln_nxt.append(count_nxt)
            day_nxt.append(x.split('\t')[0])
            month_nxt.append(x.split('\t')[1])
            year_nxt.append(x.split('\t')[2])
            name_nxt.append(x.split("\t")[5])
            rating_nxt.append(x.split("\t")[4])
            rank_nxt.append(x.split("\t")[3])

        nxt.close()

        min_rate_out = int(min(rating_nxt)) - 100
        min_rate_in = int(min(rating_cr)) - 100
    
        #fill default next image
        for k in range(0,3,1):
            DefImg[k]=name_nxt[k]

        comp_list =[]
    
        for c in range(len(name_cr)):
            check =0
            for n in range(len(name_nxt)):

                if name_cr[c] == name_nxt[n]:
                    check =1
                    row=[name_nxt[n], int(rank_cr[c]), int(rank_nxt[n]), int(rating_cr[c]), int(rating_nxt[n]), int(ln_cr[c]), int(ln_nxt[n])]
                    #print(name_nxt[n], int(rank_cr[c]), int(rank_nxt[n]), int(rating_cr[c]), int(rating_nxt[n]), int(ln_cr[c]), int(ln_nxt[n]))
                    comp_list.append(row)
            

            if check==0:
                row = [name_cr[c], int(rank_cr[c]), 12, int(rating_cr[c]), int(rating_cr[c])-200, int(ln_cr[c]), 12]
                #print(name_cr[c], int(rank_cr[c]), int(rank_cr[c])+10, int(rating_cr[c]), int(rating_cr[c])-400, int(ln_cr[c]), int(ln_cr[c])+10)
                comp_list.append(row)
        


        for n in range(len(name_nxt)):
            check =0
            for c in range(len(name_cr)):
                if name_nxt[n] == name_cr[c]:
                    check =1

            if check==0:
                row = [name_nxt[n], 12, int(rank_nxt[n]), int(rating_nxt[n])-200, int(rating_nxt[n]), 12, int(ln_nxt[n])]
                #print(name_nxt[n], int(rank_nxt[n])+10, int(rank_nxt[n]), int(rating_nxt[n])-200, int(rating_nxt[n]), int(ln_nxt[n])+10, int(ln_nxt[n]))
                comp_list.append(row)


        if name_cr == name_nxt and rank_cr == rank_nxt and rating_cr == rating_nxt and ln_cr == ln_nxt:
            animate_frames =20
        else:
            animate_frames =61
    
        for an in range(0,animate_frames+1, 1):

            day_ip=[]
            day_ip.append(day_cr[0])
        
            month_ip=[]
            if month_cr[0] == month_nxt[0]:
                mn_cr = (month_cr[0], 0)
                mn_nxt = (month_nxt[0], animate_frames)
                month_ip.append(mn_cr)
                month_ip.append(mn_nxt)
            else:
                mn_cr = (month_cr[0], an)
                mn_nxt = (month_nxt[0], animate_frames-an)
                month_ip.append(mn_cr)
                month_ip.append(mn_nxt)
                
            year_ip=[]
            if year_cr[0] == year_nxt[0]:
                yr_cr = (year_cr[0], 0)
                yr_nxt = (year_nxt[0], animate_frames)
                year_ip.append(yr_cr)
                year_ip.append(yr_nxt)
            else:
                yr_cr = (year_cr[0], an)
                yr_nxt = (year_nxt[0], animate_frames-an)
                year_ip.append(yr_cr)
                year_ip.append(yr_nxt)
            
            rank_ip=[]
            line_ip=[]
            rating_ip=[]
            name_ip=[]
            color_ip=[]

            for item in range(len(comp_list)):

                name_ip.append(comp_list[item][0])
                
                clr = color_dict[comp_list[item][0]]
                color_ip.append(clr)
            
                delta_rank = (comp_list[item][2] - comp_list[item][1])/animate_frames
                rank_new = comp_list[item][1] + (an * delta_rank)
                rank_ip.append(rank_new)

                delta_ln = (comp_list[item][6] - comp_list[item][5])/animate_frames
                ln_new = comp_list[item][5] + (an * delta_ln)
                line_ip.append(ln_new)

                delta_rating = (comp_list[item][4] - comp_list[item][3])/animate_frames
                rating_new = comp_list[item][3] + (an * delta_rating)
                rating_ip.append(rating_new)

            if animate_logo == True:
                aframe = (animate_frames, an)
            else:
                aframe = (animate_frames, animate_frames)
            
            img = get_figure(day_ip, month_ip, year_ip, line_ip, rank_ip, rating_ip, name_ip, color_ip, 40, rating_range, image_path, DefImg, aframe)

            # Convert PIL image to OpenCV format
            frame = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

            # Write the frame to the video
            video_writer.write(frame)

    # Release the video writer
    video_writer.release()

    print(f"Video saved to: {output_video_path}")
    
    return True
