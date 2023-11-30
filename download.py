import requests
import os

def download_files(url_list, download_folder, len_filename):
    # Create the download folder if it doesn't exist
    os.makedirs(download_folder, exist_ok=True)

    for url in url_list:
        try:
            # Extract the filename from the URL
            filename = os.path.join(download_folder, os.path.basename(url))
            
            # Send a GET request to the URL
            response = requests.get(url)

            original_filename = os.path.basename(url)
            new_name = original_filename[:len_filename]
                
                # Format the filename using the specified pattern
            filename = os.path.join(download_folder, new_name)

            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                # Save the content to a file
                with open(filename, 'wb') as file:
                    file.write(response.content)
                print(f"Downloaded: {filename}")
            else:
                print(f"Failed to download {url}. Status code: {response.status_code}")
        except Exception as e:
            print(f"An error occurred while downloading {url}: {str(e)}")

if __name__ == "__main__":
    # List of URLs to download, should be .xml or .bin files
    # The list of URLs can be accquired from Networks tab in Firefox developer tools
    # E.g.
    # urls = ["https://d31qrhn6llvfk5.cloudfront.net/contents/80d8/1371144/bsxmlx/3725cb1c2f066b9a928bb91bd56cd210b6298af7d19e7580ee57116a2fd69494/0043.xml?Expires=1700992896&Signature=v~PKh7PGR0NQdKJTAXWkbBWmyAckZtkkd2ayCPRPhgvqn43XUUh86eiId7D7nBNihkbvGUSuvmMq3zrJ00AxoM~GX3d7IwYhACTJQoX~3hmIiVPHS7tZxXDBUulZJ5pdHj2wQeCLi38-WE~xyRCEcqSq2gZcswwjvYPe6QfGZlOKnjcDvU3xjMa5PBR8TY~seTV8AahNT-CeKWzgBroDt2wEmKcDy1Qk4MukHcxveWBnwy4GFI69kXqLvqsVMHe9qyBVxDjRmNsbeKl8YwwIqS~nbGmMEx4~uOM1DFMQHYmUL1dnpCXYXSmhmrhfrX7C6MuDKah8iTlPiQ-90jENu7qb2IySMxVZq5bhS3aqNDanJXeYtDusZbVSGy2glvcK-BGx0RVBinFGkIosuMRbe3x4u50f~7O3zW4x9~5uyQtx3nQqWGyMJrbSiAAObJRNCL1iKav95RNmUYHIHr8OmeSMgou8xc4i4qterjP--iT~AhxygFrBhN3X7rBDFHPZ9kkcktn1ojxzGK4VWD2US4ciBleLPd8kmHp9qxEUU~EFFb7SlzLS7J51-4oPvS1C1h~pfvDbSBY0TksbMDt1yXy6z3d8fcyYnO1l3S692Oj9upedKgVgymk3hUAL-RnmZkiFkffEThIRc8k29OFQUeBSg7eJRtMHbjzVAvC2UEs_&Key-Pair-Id=APKAIXFZR6AOJBU7EAUQ"]

    urls = []
    len_filename = 13 # For .bin files in 0000_0000.bin format
    # len_filename = 8 # For .xml files in 0000.xml format
    
    # Folder to save downloaded files
    download_folder = "./Downloads/randomtitle"
    download_files(urls, download_folder, len_filename)
