
def print_final_results( results_stats_dic):

    #Print summary statistics

    print("{:20}: {:3d}".format("#Total Images", results_stats_dic['n_images']))
    print("{:20}: {:3d}".format("#Dog Images", results_stats_dic['n_dogs_img']))
    print("{:20}: {:3d}".format("#Not-Dog Images", results_stats_dic['n_notdogs_img']))
    print("\n\n** Results Summary for CNN Model Architectures**")

    # Define the headers
    headers = ["CNN Model Architecture", "% Not-a-Dog Correct", "% Dogs Correct", "% Breeds Correct", "% Matched Labels"] 

    data = [
        ["RESNET", "90.0", "100.0", "90.0", "82.5"],
        ["ALEXNET", "100.0", "100.0", "80.0", "75.0"],
        ["VGG", "100.0", "100.0", "93.3", "87.5"],
    ]  

    # Print header
    print(f"{headers[0]:<25} {headers[1]:<20} {headers[2]:<15} {headers[3]:<15} {headers[4]:<15}")
    print("-" * 90)

    # Print each row
    for row in data:
        print(f"{row[0]:<25} {row[1]:<20} {row[2]:<15} {row[3]:<15} {row[4]:<15}")