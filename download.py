import dload, requests, urllib

def DownloadImages():
    file_list = "links.txt"
    print("downloading pictures now....")
    dload.save_multi(file_list, "data/saved/", max_threads=50)
