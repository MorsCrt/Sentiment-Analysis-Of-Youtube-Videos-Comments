import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pandas as pd


links = [
    "https://www.youtube.com/watch?v=LxgMdjyw8uw",
    "https://www.youtube.com/watch?v=_Yhyp-_hX2s",
    "https://www.youtube.com/watch?v=wSN8L2SrZOg",
    "https://www.youtube.com/watch?v=X92nDeBvRnA",
    "https://www.youtube.com/watch?v=w6urQm7Prs4",
    "https://www.youtube.com/watch?v=bVEN1GwSjss",
    "https://www.youtube.com/watch?v=khF2KTyYx3Q",
    "https://www.youtube.com/watch?v=Ogcd-etnFLw",
    "https://www.youtube.com/watch?v=DPmtnb8NBog",
    "https://www.youtube.com/watch?v=5MgBikgcWnY",
    "https://www.youtube.com/watch?v=mz8jxbjP2-c",
    "https://www.youtube.com/watch?v=xGcfBRkJSWQ",
    "https://www.youtube.com/watch?v=8nXX1WOuvrk",
    "https://www.youtube.com/watch?v=NcRifDitRnU",
    "https://www.youtube.com/watch?v=9qRxNYuR2c4",
    "https://www.youtube.com/watch?v=JkaxUblCGz0",
    "https://www.youtube.com/watch?v=jXPj66c_dqA",
    "https://www.youtube.com/watch?v=_svQL2YICCI",
    "https://www.youtube.com/watch?v=3wxWNAM8Cso",
    "https://www.youtube.com/watch?v=9uUFsg3sU8E",
    "https://www.youtube.com/watch?v=rlR4PJn8b8I",
    "https://www.youtube.com/watch?v=nvzkHGNdtfk",
    "https://www.youtube.com/watch?v=iFp-L2sE-Io",
    "https://www.youtube.com/watch?v=XNTMfax5Q5w",
    "https://www.youtube.com/watch?v=kXYiU_JCYtU",
    "https://www.youtube.com/watch?v=eVTXPUF4Oz4",
    "https://www.youtube.com/watch?v=C6K_IVtGxA8",
    "https://www.youtube.com/watch?v=UDVtMYqUAyw",
    "https://www.youtube.com/watch?v=Bt5k9KLRYeU",
    "https://www.youtube.com/watch?v=827OLC8pWHA",
    "https://www.youtube.com/watch?v=0Xc4ckTTQN0",
    "https://www.youtube.com/watch?v=zodHltkgK1w",
    "https://www.youtube.com/watch?v=O2F91Up9fT8",
    "https://www.youtube.com/watch?v=-KDNFBgHdBc",
    "https://www.youtube.com/watch?v=skcqFTi3s_A",
    "https://www.youtube.com/watch?v=Yutzg2NLwcU",
    "https://www.youtube.com/watch?v=gYs_jYUyaoY",
    "https://www.youtube.com/watch?v=VXUwC9NcL0I",
    "https://www.youtube.com/watch?v=apbSsILLh28",
    "https://www.youtube.com/watch?v=5dZ_lvDgevk",
    "https://www.youtube.com/watch?v=M1-YeqGynlw",
    "https://www.youtube.com/watch?v=7xO5XRv-hXw",
    "https://www.youtube.com/watch?v=efs3QRr8LWw",
    "https://www.youtube.com/watch?v=bdqj0T6F5HU",
    "https://www.youtube.com/watch?v=RiLgp0EGdU8",
    "https://www.youtube.com/watch?v=H-qd3ySLgz4",
    "https://www.youtube.com/watch?v=YMm3yrVhA88",
    "https://www.youtube.com/watch?v=qCZAynQU_-8",
    "https://www.youtube.com/watch?v=WPni755-Krg",
    "https://www.youtube.com/watch?v=3KdmfZFKc74",
    "https://www.youtube.com/watch?v=qIQ3xNqkVC4",
    "https://www.youtube.com/watch?v=mgKFTvRwicg",
    "https://www.youtube.com/watch?v=mufeRQYgqZc",
    "https://www.youtube.com/watch?v=7xO5XRv-hXw",
    "https://www.youtube.com/watch?v=azRl1dI-Cts",
    "https://www.youtube.com/watch?v=XmtXC_n6X6Q",
    "https://www.youtube.com/watch?v=mgmVOuLgFB0",
    "https://www.youtube.com/watch?v=pUZeSYsU0Uk",
    "https://www.youtube.com/watch?v=VSaEdshUCzA",
    "https://www.youtube.com/watch?v=Unzc731iCUY",
    "https://www.youtube.com/watch?v=mPh9JZlVUK0",
    "https://www.youtube.com/watch?v=NdDU_BBJW9Y",
    "https://www.youtube.com/watch?v=ZxslGy6yg4Y",
    "https://www.youtube.com/watch?v=vDYP6AKw8bk",
    "https://www.youtube.com/watch?v=A62M_O5JpPU",
    "https://www.youtube.com/watch?v=2GC86EhnpiQ",
    "https://www.youtube.com/watch?v=BO8lX3hDU30"
]



print(len(links))
comments = list()
with Chrome() as driver:
    wait = WebDriverWait(driver,30)
    for i in links:
        driver.get(i)

        for item in range(12): 
            wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body"))).send_keys(Keys.END)
            time.sleep(10)

        for comment in wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#content-text"))):
            comments.append(comment.text)
            
df = pd.DataFrame()
df["results"] = comments
df.to_csv("temp.csv",index=False,encoding="utf-8")