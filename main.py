from matrix import create_matrix, create_utmat, convert_df, write_to_csv

if __name__ == "__main__":
    root_dir = "C:/Users/Aksha/github/IRCTCAlgorithm"
    output_dir = root_dir + "/csv"
    filename = "data.csv"
    points = ['GHY', 'BZA', 'MAS', 'HYB', 'ADI', 'NZM', 'CHTS', 'CAPE', 'MMCT', 'KOTA']
    matrix = create_matrix(10, 10)
    create_utmat(matrix)
    d_frame = convert_df(points, matrix)
    write_to_csv(output_dir, filename, d_frame)
    