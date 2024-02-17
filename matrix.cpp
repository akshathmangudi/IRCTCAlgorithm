#include <iostream>
#include <algorithm>
#include <vector>
#include <fstream>

// Implementing our basic matrix
std::vector<std::vector<int>> createMatrix(int ROWS, int COLS) {
	if (ROWS <= 0) {
		std::cout << "0 x m matrix not possible. Please retry." << std::endl;
	} else if (COLS <= 0) {
		std::cout << "n x 0 matrix is also not possible. Retry again." << std::endl;
	} else if (ROWS <= 0 && COLS <= 0) {
		std::cout << "Negative dimesnions are not possible." << std::endl;
	} else {
		return std::vector<std::vector<int>>(ROWS, std::vector<int>(COLS, 0));
	}
}

// Now to implement our upper triangular matrix
std::vector<std::vector<int>> createUTMat(std::vector<std::vector<int>>& mat) {
	int row = mat.size(); 
	int col = mat[0].size(); 
	
	// Any element above the main diagonal will be 100, rest 0
	for (int i = 0; i < row; i++) { 
		for (int j = 0; j < col; ++j) {
			if (i > j) { 
				mat[i][j] = 0;
			} else {
				mat[i][j] = 100; 
			}
		}
	}
	return mat; 
}

// Our last step is to put the vector data into the matrix
void writingToCSV(std::vector<std::vector<int>> mat, const std::string& filepath) {
	// This ofstream will write our vector data into the CSV file
	std::ofstream myFile(filepath);

	// Throw error if there's an issue with the file
	if (!myFile.is_open()) {
		std::cerr << "Unable to open file matrix.csv" << std::endl;
		return; 
	}
	
	for (auto& row : mat) { 
		for (size_t i = 0; i < row.size(); ++i) { 
			myFile << row[i]; 
			if (i != row.size() - 1) {
				myFile << ","; 
			}
		}
		myFile << "\n";
	}
	myFile.close();
}	
		

int main() {
	int ROWS = 10; 
	int COLS = 10; 
	std::string fpath = "C:/Users/Aksha/IRCTCAlgo/csv/matrix.csv";

	// Defining our matrix and transforming it into Upper Triangular
	std::vector<std::vector<int>> matrix = createMatrix(ROWS, COLS); 
	matrix = createUTMat(matrix);
	
	// Writing our matrix in a CSV file.
	writingToCSV(matrix, fpath);	

	/*
	for (auto row : matrix) {
		for (auto ele : row) { 
			std::cout << ele << " ";
		}
		std::cout << std::endl;
	}
	return 0;
       */	
	
}
