"""
 //TC#3: Google search
        //1- Open a Chrome browser
       // WebDriverManager.chromedriver().setup();
        WebDriver driver = new ChromeDriver();
        driver.manage().window().maximize();

        //2- Go to: https://google.com
        driver.get("https://google.com");

        //3- Write “apple” in search box
        //a. locate search box
        WebElement googleSearchBox = driver.findElement(By.name("q"));

        //b. enter "apple" key, and press ENTER
        googleSearchBox.sendKeys("apple" + Keys.ENTER);

        //4- Press ENTER to search
        //Thread.sleep(2000);
        //googleSearchBox.sendKeys(Keys.ENTER);

        //5- Verify title:
        //Expected: Title should start with “apple” word

        String expectedInBeginningOfTitle = "apple";
        String actualTitle = driver.getTitle();

        if (actualTitle.startsWith(expectedInBeginningOfTitle)){
            System.out.println("Title verification PASSED!");
        }else{
            System.out.println("Title verification FAIL!!!");

        }


"""
from  selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver=webdriver.Safari()
driver.maximize_window()
driver.get("https://google.com")
google_search_box=driver.find_element(By.NAME,"q")
google_search_box.send_keys("apple",Keys.ENTER)
expected_title_begin_with="apple"
actual_title=driver.title

if actual_title.startswith(expected_title_begin_with):
    print("SUCCESS")
else:
    print("FAILED")

#driver.quit()