from data_getter.image_getter import download_images_up
from data_getter.data_getter import get_cricket_rankings
from data_getter.get_item_list import get_player_list
from vidGen.render_vid import generate_animation
def main():
    print("Starting StatBox Animator")

    path_tables = "./data/tables/"
    path_images = "./data/images/"
    path_outvid = "./vidResult/"
    
    img = True
    #Download ranking tables
    start_year = 2000;
    end_year = 2001;
    ranking_tables = get_cricket_rankings(start_year, end_year, path_tables)

    if ranking_tables > 0:
        print("Downloaded all files")
        #Get Item list for images and dictionaries
        items = get_player_list(ranking_tables, path_tables)

        if not img:
            try:
                print("Trying to download images")
                for item in items:
                    search_query = item
                    search_relevance = "ESPNcricinfo profile picture"
                    download_images_up(search_query, search_relevance, path_images)

            except Exception as e:
                print("Error while trying to download images:", e)
                print("Please try to download the images manually")

        
        #Generate Video
        generate_animation(ranking_tables, path_tables, path_images, path_outvid)


if __name__ == "__main__":
    main()
