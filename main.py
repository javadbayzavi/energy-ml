from nltk.tokenize import word_tokenize
text="""Software design patterns (DPs) are reusable solutions which proposed 
to overcome the complexity of the software design and development processes. 
However, the implementation effectiveness of the use of these patterns is in 
question for many communities and developers. In the first instance, recognizing 
DPs in source code helps in improving the aspects of reusability and maintainability
 that play an essential role during analysis and design phases of software 
 development process. Various studies have been published in the area of design 
 pattern detection (DPD) to emphasize the importance of research in this field. 
 Some studies focused on a specific programming language, whereas the others 
 concentrated on set of patterns. In terms of detection mechanisms, various 
 researches developed machine learning approaches to analyze the source code and 
 extract defined patterns. However, these works dismiss the fact that a software 
 project is not only a directory of source files and documents. While several 
 research works have attempted to detect the presence of these patterns, they 
 suffer from the lack of investigating the software application as a whole. 
 In fact, in a holistic view, everything started from requirement engineering 
 among user requests and feedbacks. Besides, the contribution of development 
 teams can have direct effects on the way software projects are using DPs. 
 In this regard, this study aims at using machine learning and text processing 
 techniques to detect and extract all useful material related to DPs within 
 public project repositories, from source code to user feedbacks and submitted 
 issues. Indeed, the research directs its efforts in two specific areas: 1. source code 
 evaluation for DPD, 2. software issue list and pull requests evaluation for 
 interested discussions about DPs. Our contributions include a) the design and 
 development of novel approaches for detecting DPs using machine learning 
 algorithms, b) the identification of flaws and improvement opportunities 
 in the use of DPs and c) the operationalization of a tool that integrates 
 approaches mentioned in a and b. The result of both analysis will be subject 
 to statistical and prediction studies, towards establishing that DPs positively 
 impact the overall quality of the software.  """

tokenized_words = word_tokenize(text)

from nltk.probability import FreqDist
fdist = FreqDist(tokenized_words)

import matplotlib.pyplot as plt
fdist.plot(30,cumulative=False)
plt.show()