1.	Load Data set
2.	Initialize General Hypothesis and Specific Hypothesis.
3.	For each training example  
4.	If example is positive example  
          if attribute_value == hypothesis_value:
             Do nothing  
          else:
             replace attribute value with '?' (Basically generalizing it)
5.	If example is Negative example  
          Make generalize hypothesis more specific.
