Cash Flow Minimizer System for Inter-Bank Transactions

This system minimizes the number of transactions among multiple banks in different corners of the world that use different modes of payment. There is one world bank (with all payment modes) to act as an intermediary between banks that have no common mode of payment.

Getting Started

Let's take an example. Suppose we have the following banks:

Bank_of_America (World Bank)
Wells_Fargo
Royal_Bank_of_Canada
Westpac
National_Australia_Bank
Goldman_Sachs

Following are the payments to be done:

Debtor Bank	              Creditor Bank        	  Amount

Goldman_Sachs	            Bank_of_America	        Rs 100
Goldman_Sachs	            Wells_Fargo	            Rs 300
Goldman_Sachs	            Royal_Bank_of_Canada	  Rs 100
Goldman_Sachs	            Westpac	                Rs 100
National_Australia_Bank	  Bank_of_America	        Rs 300
National_Australia_Bank	  Royal_Bank_of_Canada 	  Rs 100
Bank_of_America	          Wells_Fargo	            Rs 400
Wells_Fargo	              Royal_Bank_of_Canada	  Rs 200
Royal_Bank_of_Canada	    Westpac	                Rs 500


Test Cases

Test Case 1:

Input:
5
A 2 t1 t2
B 1 t1
C 1 t1
D 1 t2
E 1 t2
4
B A 300
C A 700
D B 500
E B 500

Output:

The transactions for minimum cash flow are as follows:

D pays Rs 500 to A via t2
E pays Rs 500 to A via t2
C pays Rs 200 to A via t1
C pays Rs 500 to B via t1

Test Case 2:

Input:
5
World_Bank 2 Google_Pay PayTM
Bank_B 1 Google_Pay
Bank_C 1 Google_Pay
Bank_D 1 PayTM
Bank_E 1 PayTM
4
Bank_B World_Bank 300
Bank_C World_Bank 700
Bank_D Bank_B 500
Bank_E Bank_B 500

Output:
The transactions for minimum cash flow are as follows:

Bank_D pays Rs 500 to World_Bank via PayTM
Bank_E pays Rs 500 to World_Bank via PayTM
Bank_C pays Rs 200 to World_Bank via Google_Pay
Bank_C pays Rs 500 to Bank_B via Google_Pay


Test Case 3:

Input:
6
B 3 1 2 3
C 2 1 2
D 1 2
E 2 1 3
F 1 3
G 2 2 3
9
G B 30
G D 10
F B 10
F C 30
F D 10
F E 10
B C 40
C D 20
D E 50

Output:
The transactions for minimum cash flow are as follows:

F pays Rs 10 to D via 3
F pays Rs 10 to E via 3
G pays Rs 10 to D via 2
G pays Rs 10 to B via 2
G pays Rs 10 to B via 3
F pays Rs 30 to C via 3
B pays Rs 30 to C via 1
C pays Rs 20 to D via 2
D pays Rs 50 to E via 2


