Phase 2 of the project involves determining similarity measures for the feature set(Color histogram, SIFT and motion vectors)
and using these distance measures to determine k similar frames between videos vi and vj

Please find below instructions to run files for tasks done as part of the project:
Task 1:
		Given color histogram, SIFT vector and motion vectors in files out_file.chst, out_file.sift and out_file.mvect respectively in the format
		below for every line in the file:
		Color Histogram:Video Number;Frame Number;Cell Number;N-bin color histogram value
		SIFT:Video Number;Frame Number;Cell Number;sift vector(x,y,scale,orientation,a1...128-keypoint descriptor)
		Motion vector:Video Number;Frame Number;Cell Number; motion vector (source,width,height, srcx,srcy,dstx,dsty)

		Task 1 computes similarity measure between video files vi and vj by considering one of these features as well as all of the features
		depending on parameters passed to the python file.
	
	task1.py-The file which is used to determine similarity measure for the videos. Takes the following parameters:
	task1 <subtask-id> <id1> <id2>
	subtask-id can have the following values(in braces the features and distance measure used for similarity measurement):
		1a(Color Histogram using	Intersection Similarity)
		1b(Color Histogram using	Cosine Similarity)
		1c(SIFT  using	Intersection Similarity)
		1d	(SIFT Vectors using	Mahalanobis Distance)
		1e	(Motion Vectors using	L1 Distance)
		1f	(Motion Vectors using	Cosine Similarity)
		1g	(Color Histogram, SIFT and Motion Vectors using	Intersection Similarity)
		1h	(Color Histogram, SIFT and Motion Vectors using	L1 Distance)
	id1 - video number identifying the video in directory(0-no:of videos in directory-1) 
	id2 - video number identifying the video in directory(0-no:of videos in directory-1)
	When valid parameters are provided for task1, it displays the distance measure for the videos based on the sutask-id selected
	
Task 2:
		Given color histogram, SIFT vector and motion vectors in files out_file.chst, out_file.sift and out_file.mvect respectively in the format
		below for every line in the file:
		Color Histogram:Video Number;Frame Number;Cell Number;N-bin color histogram value
		SIFT:Video Number;Frame Number;Cell Number;sift vector(x,y,scale,orientation,a1...128-keypoint descriptor)
		Motion vector:Video Number;Frame Number;Cell Number; motion vector (source,width,height, srcx,srcy,dstx,dsty)

		Task 2 identifies and displays k most similar frame sequences and visualizes the query and results as videos by considering distance
		measures between videos
	
	task2.py-The file which is used to do video subsequence search. Takes the following parameters:
	task2 <subtask-id> <id> <start> <end> <path> <no of subsequences to display>
	subtask-id can have the following values(in braces the features and distance measure used for similarity measurement):
		1a(Color Histogram using	Intersection Similarity)
		1b(Color Histogram using	Cosine Similarity)
		1c(SIFT  using	Intersection Similarity)
		1d	(SIFT Vectors using	Mahalanobis Distance)
		1e	(Motion Vectors using	L1 Distance)
		1f	(Motion Vectors using	Cosine Similarity)
		1g	(Color Histogram, SIFT and Motion Vectors using	Intersection Similarity)
		1h	(Color Histogram, SIFT and Motion Vectors using	L1 Distance)
	id- video number identifying the video in directory(0-no:of videos in directory-1)
	start - start video frame number
	end - end video frame number
	path - directory containing video files
	no of subsequences to display - the number of subsequences matched to return
	When valid parameters are provided, Task 2 displays the displays for the top k similar subsequence distance measure and displays those subsequences to the user

Task 3:
		Given color histogram, SIFT vector and motion vectors in files out_file.chst, out_file.sift and out_file.mvect respectively in the format
		below for every line in the file:
		Color Histogram:Video Number;Frame Number;Cell Number;N-bin color histogram value
		SIFT:Video Number;Frame Number;Cell Number;sift vector(x,y,scale,orientation,a1...128-keypoint descriptor)
		Motion vector:Video Number;Frame Number;Cell Number; motion vector (source,width,height, srcx,srcy,dstx,dsty)

		Task 3 reduces the dimensionality to d- the given dimensionality and reports the input vector space in the given dimension space along with the score for the new dimenisons
		in terms of the old dimension. The following files perform dimension reduction/ score reporting for the features present.
		
		pcaHist.py-Performs dimensionality reduction using PCA for color histogram for user input d and saves the vector space in terms in the new dimension in out_file_d.cpca in 
		following format for each row of the file:
		Video Number;Frame Number;Cell Number;reduced dimension histogram values
		The score for each of the new dimension is reported in the file histdcomp.cpca with each line representating the new dimension
		with (original_index,score) value for each of the contributing index
		
		pcaSift.py-Performs dimensionality reduction using PCA for SIFT vector for user input d and saves the vector space in terms in the new dimension in out_file_d.spca in 
		following format for each row of the file:
		Video Number;Frame Number;Cell Number;reduced dimension SIFT values
		The score for each of the new dimension is reported in the file siftdcomp.spca with each line representating the new dimension
		with (original_index,score) value for each of the contributing index
		
		pcaMotion.py-Performs dimensionality reduction using PCA for motion vector for user input d and saves the vector space in terms in the new dimension in out_file_d.mpca in 
		following format for each row of the file:
		Video Number;Frame Number;Cell Number;reduced dimension motion vector values
		The score for each of the new dimension is reported in the file motiondcomp.mpca with each line representating the new dimension
		with (original_index,score) value for each of the contributing index
		
		kmeansHist.py-Performs dimensionality reduction using k-means for color histogram for user input d and saves the vector space in terms in the new dimension in out_file_d.ckm in 
		following format for each row of the file:
		Video Number;Frame Number;Cell Number;reduced dimension histogram values
		The score for each of the new dimension is reported in the file histdcomp.ckm with each line representating the new dimension
		with (original_index,score) value for each of the contributing index
		
		kmeansSift.py-Performs dimensionality reduction using k-means for SIFT vector for user input d and saves the vector space in terms in the new dimension in out_file_d.skm in 
		following format for each row of the file:
		Video Number;Frame Number;Cell Number;reduced dimension SIFT values
		The score for each of the new dimension is reported in the file siftdcomp.skm with each line representating the new dimension
		with (original_index,score) value for each of the contributing index
		
		kmeansMotion.py-Performs dimensionality reduction using k-means for motion vector for user input d and saves the vector space in terms in the new dimension in out_file_d.mkm in 
		following format for each row of the file:
		Video Number;Frame Number;Cell Number;reduced dimension motion vector values
		The score for each of the new dimension is reported in the file motiondcomp.mkm with each line representating the new dimension
		with (original_index,score) value for each of the contributing index

Task 4:
		Given the reduced dimesion data from task 3 determine and displays k most similar frame sequences and visualizes the query and results as videos by considering distance
		measures between  from task 1.
		
		task2.py-The file which is used to do video subsequence search. Takes the following parameters:
		task2 <subtask-id> <id> <start> <end> <path> <no of subsequences to display>
		subtask-id can have the following values(in braces the features and distance measure used for similarity measurement):
		1a(Color Histogram using	Intersection Similarity)
		1b(Color Histogram using	Cosine Similarity)
		1c(SIFT  using	Intersection Similarity)
		1d	(SIFT Vectors using	Mahalanobis Distance)
		1e	(Motion Vectors using	L1 Distance)
		1f	(Motion Vectors using	Cosine Similarity)
		1g	(Color Histogram, SIFT and Motion Vectors using	Intersection Similarity)
		1h	(Color Histogram, SIFT and Motion Vectors using	L1 Distance)
		id- video number identifying the video in directory(0-no:of videos in directory-1)
		start - start video frame number
		end - end video frame number
		path - directory containing video files
		no of subsequences to display - the number of subsequences matched to return
		When valid parameters are provided, Task 4 displays the displays for the top k similar subsequence distance measure and displays those subsequences to the user
