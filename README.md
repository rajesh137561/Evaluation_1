# Evaluation_1
#Question 1 : Write a regex to extract all the numbers with orange color background from the below text in italics.

{"orders":[{"id":1},{"id":2},{"id":3},{"id":4},{"id":5},{"id":6},{"id":7},{"id":8},{"id":9},{"id":10},{"id":11},{"id":648},{"id":649},{"id":650},{"id":651},{"id":652},{"id":653}],"errors":[{"code":3,"message":"[PHP Warning #2] count(): Parameter must be an array or an object that implements Countable (153)"}]}

Answer : The code does the same. I used regex along with checking the condition that the digits need to begin with a :

#Question 2 : Problem statement - There are times when a user writes Good, Nice App or any other positive text, in the review and gives 1-star rating. Your goal is to identify the reviews where the semantics of review text does not match rating. Your goal is to identify such ratings where review text is good, but rating is negative- so that the support team can point this to users. Deploy it using - Flask/Streamlit etc and share the live link. 

Answer : I have shared the code here in gitlab. The datasets used is the same which was provided. The overall idea is as follows.
1. Read data from csv using pandas
2. Extract useful columns
3. Convert rating to a positivity score - which denotes the class to which it belongs to. Rating of above 3 is classified as 1, other ratings as 0.
4. Use NLP tools to learn semantics of the review texts .we used NLTK which helped in cleaning the data and creating a corpus of useful words. Each review form the data point and column entries are all possible words with 0s if not a part of the text and 1s if part of the text. This semantic overview of the text helps in having a correlation between good review and good rating, and bad vs bad.
5. Then, we train the model using random forests.

Part 2 : Check if the sentence is Grammatically correct: Please use any pre-trained model or use text from open datasets. Once done, please evaluate the English Grammar in the text column of the below dataset. 

Answer : I have used pretrained language-tool for performing the grammar check. I have used the language_tool_python wrapper for the well-known Java LanguageTool. I accept the input as pandas dataframe and keep only the review text column, and pass this text one by one to the language tool to evaluate the grammatical correctness. If there are no mistakes - we print no mistakes, else the number of mistakes detected would be printed.

#Question : 2Formally, a vector space V' is a subspace of a vector space V if
V' is a vector space
every element of V′ is also an element of V.
Note that ordered pairs of real numbers (a,b) a,b∈R form a vector space V. Which of the following is a subspace of V?
The set of pairs (a, a + 1) for all real a
The set of pairs (a, b) for all real a ≥ b
The set of pairs (a, 2a) for all real a
The set of pairs (a, b) for all non-negative real a,b

Answer :  For a subspace H to be a vector space by itself, it has to fulfil the following 3 criteria.
(i)	Zero - The zero vector of vector space V must also be in H
(ii)	Addition - For each u,v in H, u+v is also in H.
(iii)	Scalar multiplication - For each u in H and a scalar c, cu is also in H.
Let us consider each of the above sets and discuss whether they form a subspace of V
•	The set of pairs (a, a + 1) for all real a
clearly (0,0) which is the zero of vector space V is not in this set. So it can’t be a subspace
•	The set of pairs (a, b) for all real a ≥ b
It meets the first two criteria discussed above. It has the zero vector (0,0) in it. It also satisfies the addition rule. But it fails to meet the scalar multiplication rule. Ex: let c = -5, u = (4,3) cu = (-20,-15) which is not an element of the given set.
•	The set of pairs (a, 2a) for all real a
It meets all the 3 criteria. It has the zero vector (0,0) in it. It meets the addition rule. Ex: for any u = (a,2a) and v = (b,2b), u+v = (a+b, 2(a+b)) which belongs to the given set. It also meets the scalar multiplication criterion. For any u = (a,2a), cu = (ca, 2ca) which belongs to the given set. So, the set of pairs (a,2a) for all real a, form the subspace of vector space V.
•	The set of pairs (a, b) for all non-negative real a,b
It satisfies the first two criteria for being a subspace as it contains both zero vector and satisfies the addition rule for all the elements in the set. But it fails to meet the scalar multiplication criterion, for a choice of negative value for scalar c. ex: if c = -1, an element of the set u = (3,4) , cu = (-3,-4) which is not a member of the given set.





