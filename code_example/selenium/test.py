
from selenium import webdriver  
import time  
import os  
  
profile_dir=r"C:\Users\pc\AppData\Local\Google\Chrome\User Data"    
chrome_options=webdriver.ChromeOptions()  
chrome_options.add_argument("user-data-dir="+os.path.abspath(profile_dir))  
  
browser=webdriver.Chrome(chrome_options=chrome_options)  
browser.maximize_window()  
browser.get("https://sellercentral.amazon.com/ap/signin?openid.pape.max_auth_age=18000&openid.return_to=https%3A%2F%2Fsellercentral.amazon.com%2Fgp%2Fhomepage.html%3Fcor%3Dlogin_NA&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=sc_na_amazon_v2&_encoding=UTF8&openid.mode=checkid_setup&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&language=zh_CN&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&pageId=sc_na_amazon&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&ssoResponse=eyJ6aXAiOiJERUYiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiQTI1NktXIn0.eHVBy96foS273JCVBlTHBQWdvkwXcC8pKeWZLdQEaWD4nT_2kIRCcQ.C7-TyBbb_A_YIkXn.8XMTkG05p58OMjaurYPZYHZuvohMFE8TBz5bKerZBwh5uY7AHFuN3-kzWfAHRlqPJzcb93HdtK2V04yJh8-vOAM6bgiZ19E32jZ41ipIkRKFa1yCtKh_sysw3_ibhVZiY51V-b5TZov5eGDqTvpgGdRJ7oy-f1QxNdUD5AT0FSMl8DKFm8D9XYJv-Ov6mHyrWrRkTSnMpT70DRrU2pbmcJmbeb--YGknamrs5TVjTIm-OZL9f-HtEXdcnFjq0voUeYFvY2gZul2VdAvsTIEAliGpgTp3vpOMEpS_DIrmVNY5LBKt-H4QBbx6cRyUIFqSzvNq-aQ5jpezVh3yveVkK9z3OBLH_mCJ2Up15yPrO2MjD8YjRYJUhrAJsetfkHg95s7orZoNBM1cgrtXIciF26poP8IGT1i-rSQ-5qOVhtWzh50luh9mXsoXkkNhHSq5haHf70kWKzXAgO8ZTgCIj_SjueoxwTY7faLdlC_fFF2MGP9xQGTglnafmjXUVm9J1m2tzeymVHqc5h4GGMwbB5tZAglCzjXeUrCwnoeKY7YjujQB_ecDIXpmICR6Wcnk-vSg7r5P_xxMrAULzW3MkEy7lBOYXCInCYi-D8xQ4VqVajjINu3Zx36oKKm57i21bDx8vimHfpMywrubzSmRtu8pzh9IZNNKx-J113GWVMTeK1jjavTLOJVsv6zEWoiv4xbrlscePPPYtab9D4MiKxWao1dw79xDZbnOVBWlS1orNznBQBPGuotCOy8.MdImhqZCl8ZKEmu8PCriFw") 

time.sleep(1000)
browser.close()