Phase 3 of the project involves experimenting with clustering, indexing, classification and relevance feedback

Please find below instructions to run files for tasks done as part of the project:
Task 1:
		Given SIFT vector file_name.sift in the format below for every line in the file:
		SIFT:Video Number;Frame Number;Cell Number;sift vector(x,y,scale,orientation,a1...128-keypoint descriptor)

		Task 1 reduces the dimensionality to d- the given dimensionality and reports the input vector space in the given dimension space along with the score for the new dimenisons
		in terms of the old dimension. The following files perform dimension reduction/ score reporting for the features present.
		
		pcaSift.py-Performs dimensionality reduction using PCA for SIFT vector for user input d and saves the vector space in terms in the new dimension in out_file_d.spca in 
		following format for each row of the file:
		Video Number;Frame Number;Cell Number;reduced dimension SIFT values
		The score for each of the new dimension is reported in the file filename_d.spc with each line representating the new dimension
		with (original_index,score) value for each of the contributing index
		

Task 2:
		Given the output filename_d.spc from Task 1 determine similarity between videos and generate a graph for k similar video frames where is given as input
		Each line in input file is of the format:
		Video Number;Frame Number;Cell Number;reduced dimension SIFT values
		
		task2.py - Performs similarity calculation for frames and assigns a similarity score for pairs of videos. It writes the output to filename_d_k.spc with each line having
		the following format:
		<ia,ja>;<ib,jb>;similarity - where ia,ja and ib,jb are the (index of video file, frame no) for videos a and b and sim is the similarity measure between the two.

Task 3a: 

		Does most significant frame selection using page rank by taking input from output file of Task 2
		Example usage of pagerank.py file that does this operation:

		C:\D-Drive\studies\MCS\MWDB\Project\Phase3_bharath\task34>python pagerank.py and an integer m
		What you want to run(Enter 1 or 2)? 1.PageRank or 2.RPR : 1
		Please enter video DB Path with trailing slash: C:\D-Drive\studies\MCS\MWDB\Project\Phase3_bharath\DemoVideos\DemoVideos\
		Please enter top-D ranking frames to show: 20
		Enter the path of the graph file : C:\D-Drive\studies\MCS\MWDB\Project\Phase3_bharath\InputOutputFiles\filename_d_k_2.gspc
		
		It visualizes the frames that were similar

Task 3b:
		Does most significant frame selection using ASCOS++ by taking input from output file of Task 2 an integer m 
		Example usage of ascosplus.py file that does this operation:
		C:\D-Drive\studies\MCS\MWDB\Project\Phase3_bharath\task34>python ascosplus.py
		Please enter video DB Path with trailing slash: C:\D-Drive\studies\MCS\MWDB\Project\Phase3_bharath\DemoVideos\DemoVideos\
		Please enter top-D ranking frames to show: 20
		Enter the path of the graph file : C:\D-Drive\studies\MCS\MWDB\Project\Phase3_bharath\InputOutputFiles\filename_d_k_2.gspc
		
		It visualizes the frames that were similar

Task 4a:

		Does most relevant frame selection using page rank by taking input from output file of Task 2, an integer m and 3 frames
		Example usage of pagerank.py file that does this operation:
		
		C:\D-Drive\studies\MCS\MWDB\Project\Phase3_bharath\task34>python pagerank.py
		What you want to run(Enter 1 or 2)? 1.PageRank or 2.RPR : 2
		Please enter video DB Path with trailing slash: C:\D-Drive\studies\MCS\MWDB\Project\Phase3_bharath\DemoVideos\DemoVideos\
		Please enter top-D ranking frames to show: 20
		Enter the path of the graph file : C:\D-Drive\studies\MCS\MWDB\Project\Phase3_bharath\InputOutputFiles\filename_d_k_2.gspc
  		normalizedSim = similarityMatrix / np.sum(similarityMatrix,axis=0)
		Enter the 3 seed frames: Video number followed by Frame number
		Enter the video number: 3
		Enter the frame number: 1
		Enter the video number: 1
		Enter the frame number: 5
		Enter the video number: 7
		Enter the frame number: 8

Task 4b:

		Does most relavent frame selection using ASCOS++ by taking input from output file of Task 2, an integer m and 3 frames
		Example usage of ascosplus.py file that does this operation:

C:\D-Drive\studies\MCS\MWDB\Project\Phase3_bharath\task34>python ascosmodified.py

Please enter video DB Path: C:\D-Drive\studies\MCS\MWDB\Project\Phase3_bharath\DemoVideos\DemoVideos\

Please enter top-D ranking frames to show: 20

Enter the path of the graph file : C:\D-Drive\studies\MCS\MWDB\Project\Phase3_bharath\InputOutputFiles\filename_d_k_2.gspc

ascosmodified.py:113: RuntimeWarning: invalid value encountered in true_divide

  normalizedSim = similarityMatrix / np.sum(similarityMatrix,axis=0)

Enter the 3 seed frames: Video number followed by Frame number

Enter the video number: 3

Enter the frame number: 1

Enter the video number: 1

Enter the frame number: 5

Enter the video number: 7

Enter the frame number: 8

Task 5,6 : Creates the LSH data file by taking input from task1

C:\D-Drive\studies\MCS\MWDB\Project\Phase3_bharath\Phase3_2.0>python task5.py -h

Usage: task5.py [options]

Options:

  -h, --help      show this help message and exit

  -I INFILEPATH   Input file name of the form filename_d.spca, default name

                  out_file_d.spca

  -L NOOFLAYERSL  Number of layers L, default value=3

  -K NOOFBITS     Number of buckets per layer, 2^K, default value=15

  -O OUTFILEPATH  Output File of the form filename_d.lsh, default name of the

                  form InputFileName_d.lsh

  -D GRIDSIZE     Size of each grid D, default value=0.12

  -M              Define whether to use Mahalanobis Distance over Euclidean,

                  The option is Disabled

  -b BAND         No. of Bits each hash function contributes, Default value=2

C:\D-Drive\studies\MCS\MWDB\Project\Phase3_bharath\Phase3_2.0>python task6.py

Usage:   python task5.py InputFile n i j x1 y1 x2 y2 Demo_Videos_Directory

Where

         - InputFile is the path to one of the output files generated by Task 5

         - 'n' represents the no. of frames containing similar objects

         - i and j represent the query video and frame no. (Videos in the directory will be of the form 'i.mp4')

         - (x1,y1) form the coordinates of one of the vertices of the rectangle containing the object to be queried in the given video and frame

         - (x2,y2) form thecoordinates of the vertex that is diagonally opposite to (x1,y1)

         - Demo_Videos_Directory is the path to the directory (without spaces) containing the given Demo Videos


