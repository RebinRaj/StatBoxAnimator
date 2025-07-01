from PIL import Image, ImageDraw, ImageFont, ImageFilter

def get_img():
    img = Image.open("./background/new_background.png").convert("RGBA")
    return img

def get_def_img(res):
    img = Image.new("RGBA", res, (0, 0, 0, 0))
    return img

def get_font(fn_size, fn_type):
    font = ImageFont.load_default()
    font = ImageFont.truetype(fn_type, fn_size)
    return font

def get_item_img(name, sz):
    path = name
    it_img = Image.open(path)
    newsize = (sz[0], sz[1])
    it_img = it_img.resize(newsize)
    it_mask = Image.new("L", it_img.size, 0)
    draw = ImageDraw.Draw(it_mask)
    draw.ellipse((20, 20, sz[0]-20, sz[1]-20), fill=255)
    it_mask_blur = it_mask.filter(ImageFilter.GaussianBlur(10))
    item_img = (it_img, it_mask_blur)
    return item_img

def get_podium(size):
    pd = Image.open("./background/my_podium_n2.png").convert("RGBA")
    pd = pd.resize(size)
    return pd

def get_figure(day, month, year,line, rank, rating, name, nclr, font_sz, limits, ImgPath, defImg, aframe):

    #items=len(rank)
    items=10
    #Color parameters
    color = (0, 0, 0)
    transparency = 0.15
    opacity = int(255 * transparency)
    rec_fill = color + (opacity,)
    
    fig = get_img()
    width, height = fig.size

    overlay = get_def_img(fig.size)
    draw = ImageDraw.Draw(overlay)
    
    frame_sz = 20
    frame_border = [frame_sz, frame_sz, width-frame_sz, height-frame_sz]
    draw.rectangle(frame_border, fill=None, outline="White", width=2)

    #Parameters for the rectangles in the rows
    space_ht = height - (2*frame_sz)                             #space of frame - endgap
    space_wd = width - (2*frame_sz)                              #space of frame - endgap

    sl_gap = 10                                                  #scale for gap w.r.t row height
    rec_ht = (space_ht*sl_gap)/(items*sl_gap + items + 1)        #row height w.r.t items
    rec_wd = space_wd - (0.3*space_wd)                           #row width
    gap = rec_ht/sl_gap                                          #gap scaled
    column1 = 50
    column2 = 460

    sframe = [rec_wd+gap, frame_sz+gap, width-frame_sz-gap, height-frame_sz-gap-750]
    sframe2 = [rec_wd+gap, frame_sz+gap+770, width-frame_sz-gap, height-frame_sz-gap]
    tr = 0.30
    op = int(255 * tr)
    scolor = (0,0,0)
    sfill = scolor + (op,)
    scolor2 = (255, 25, 255)
    sfill2 = scolor2 + (opacity,)
    draw.rectangle(sframe, fill=sfill, outline=None, width=1)
    draw.rectangle(sframe2, fill=sfill, outline=None, width=1)
    syc = frame_sz+gap+40
    font_type = "RobotoCondensed-Regular.ttf"
    fty = "OpenSans-CondLight.ttf"
    fn_bold ="RobotoCondensed-Bold.ttf"
    draw.text((rec_wd+gap+130,syc), "ICC ODI", fill='cyan', font=get_font(100, fn_bold))
    draw.text((rec_wd+gap+110,syc+110), "Batsmen Ranking", fill='cyan', font=get_font(50, font_type))
    draw.text((rec_wd+gap+210,syc+165), "1990 - 2000", fill='cyan', font=get_font(30, font_type))

    #Day and year
    anf = aframe[0]
    yr_stp = 300/anf
    yr_dwn = year[0][1]*yr_stp
    mn_stp = 300/anf
    mn_dwn = month[0][1]*mn_stp
    draw.text((rec_wd+gap+20,syc+755+yr_dwn), year[0][0], fill='cyan', font=get_font(150, fty))
    draw.text((rec_wd+gap+300,syc+825+mn_dwn), month[0][0], fill='cyan', font=get_font(70, fty))

    yr_up = year[1][1]*yr_stp
    mn_stpx = 400/anf
    mn_up = month[1][1]*mn_stpx
    draw.text((rec_wd+gap+20,syc+755+yr_up), year[1][0], fill='cyan', font=get_font(150, fty))
    draw.text((rec_wd+gap+300+mn_up,syc+825), month[1][0], fill='cyan', font=get_font(70, fty))
    #draw.ellipse((rec_wd+gap+370, syc+880, rec_wd+gap+450, syc+940), fill=(255, 255, 255,60), outline=None)
    #draw.text((rec_wd+gap+390,syc+885), day[0], fill='black', font=get_font(40))

    #my logo
    anfr_no = aframe[1]
    start_point1 = (rec_wd+gap+490-60, syc+770-25)
    end_point1 = (rec_wd+gap+490+10, syc+770-25)
    start_point2 = (rec_wd+gap+490+10, syc+770+25)
    end_point2 = (rec_wd+gap+490-60, syc+770+25)

    tr_x = (end_point1[0]-start_point1[0])/anf
    l1_anf = (start_point1[0]+(tr_x*anfr_no), end_point1[1])
    draw.line([start_point1, l1_anf], fill='cyan', width=3)

    tr_y = (end_point2[1]-start_point1[1])/anf
    l2_anf = (end_point2[0], start_point1[1]+(tr_y*anfr_no))
    draw.line([start_point1, l2_anf], fill='cyan', width=3)

    l3_anf = (start_point2[0]-(tr_x*anfr_no), end_point2[1])
    draw.line([start_point2, l3_anf], fill='cyan', width=3)

    ed1 = (end_point1[0], end_point1[1]+40)
    tr_v1 = (start_point2[1]-ed1[1])/anf
    l3_anf = (start_point2[0], start_point2[1]-(tr_v1*anfr_no))
    draw.line([start_point2, l3_anf], fill='cyan', width=3)

    fr=35
    if anfr_no>fr:
        ed2 = (end_point1[0], end_point1[1]+10)
        tr_v2 = (end_point1[1]-ed2[1])/(anf-fr)
        l3_anf = (ed2[0], ed2[1]+(tr_v2*(anfr_no-fr)))
        draw.line([ed2, l3_anf], fill='cyan', width=3)

    lbg = [start_point1[0]+5, start_point1[1]+5, start_point2[0]-5,start_point2[1]-5]
    tr_lbg = (lbg[2]-lbg[0])/anf
    lbg_anf = [lbg[0], lbg[1], lbg[0]+(tr_lbg*anfr_no), lbg[3]]
    draw.rectangle(lbg_anf, fill=sfill2, outline=None, width=1)
    draw.text((rec_wd+gap+440,syc+750), "StatBox", fill='white', font=get_font(35, "GentiumPlusCompact-R.ttf"))
    
    Font = get_font(font_sz, font_type)

    #Paste podium image with hard coded positions
    podium_pos = (1322, 500)  #hard coded
    item_pos =((1480,310), (1650, 415), (1340, 485)) #hard coded
    sc = 0.84
    pd_image = get_podium((int(673*sc),int(313*sc)))
    fig.paste(pd_image, podium_pos, pd_image)

    top_three=["Item", "Item", "Item"]
    
    for i in range(len(rank)):

        #Write elements from the file
        n1 = float(rank[i])
        n1_l= float(line[i])
        item_name = name[i]
        text = item_name.strip()
        n2 = float(rating[i])
        
        pos = n1_l*gap + (n1_l-1)*rec_ht

        #print(f"i: {i}")
        k =i+1
        x0 = 2*frame_sz
        y0 = frame_sz + pos
        x1 = rec_wd
        y1 = y0 + rec_ht
        

        xw = x0 + 15
        yw = (y0 + y1)/2 - font_sz/2
        

        #limits draw
        scale = (x1 - 80 - xw - column2)/(limits[1] - limits[0])
        val = scale * (n2-limits[0])
        ysub = rec_ht/2.8

        if val < 0:
            val=20

        clr = nclr[i]
        border = (xw+column2, y0+10, val+xw+column2, y1-10)
        rec = [x0, y0, val+xw+column2+3, y1]
        draw.rectangle(rec, fill=rec_fill, outline="White", width=1)

        draw.text((xw,yw), str(round(n1)), fill='black', font=Font)
        draw.text((xw+column1,yw), text, fill='black', font=Font)
        
        draw.rectangle(border, fill=clr, outline="black", width=1)
        #draw.rectangle(border, fill="green", outline="White", width=1)
        draw.text((val+xw+column2+5,yw), str(round(n2)), fill='black', font=Font)

        if round(n1_l)==1:
            top_three[0]=text
        if round(n1_l)==2:
            top_three[1]=text
        if round(n1_l)==3:
            top_three[2]=text


    item = ImgPath
    for itn in range(len(top_three)):
        if top_three[itn]=="Item":
            top_three[itn]=defImg[itn].strip()
        item_fr = ImgPath.format(top_three[itn])
        size = (220,220)
        it_image = get_item_img(item_fr, size)
        fig.paste(it_image[0], (item_pos[itn][0], item_pos[itn][1]), it_image[1])
        
    fig = Image.alpha_composite(fig, overlay)

    #podium_path = "./background/podium_tr.png"
    #pd_image = get_item_img(podium_path, (420, 250))
    
    return fig
