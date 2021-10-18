class common_locators:
    your_logo_xpath = "//img[@alt='My Store']"
    call_us_now_xpath = '//*[@id="header"]/div[2]/div/div/nav/span'
    cart_xpath = '//*[@id="header"]/div[3]/div/div/div[3]/div'
    women_xpath = "//a[@title='Women']"
    dress_xpath = '//*[@id="block_top_menu"]/ul/li[2]/a'
    tshirt_xpath = '//*[@id="block_top_menu"]/ul/li[3]/a'
    signin_xpath = "//a[normalize-space()='Sign in']"

    email_xpath = "//input[@id='email_create']"
    account_create = "//span[normalize-space()='Create an account']"
    account_create_header = "//h1[normalize-space()='Create an account']"

    account_title_radio_MR_xpath = "//input[@id='id_gender1']"
    account_first_name_xpath = '//*[@id="customer_firstname"]'
    account_last_name_xpath = '//*[@id="customer_lastname"]'
    account_password_xpath = "//input[@id='passwd']"
    account_DOB_date_xpath = '//*[@id="days"]'
    account_DOB_days_01_xpath = '//*[@id="days"]/option[2]'
    account_DOB_month_january_xpath = '//*[@id="months"]/option[2]'
    account_DOB_year_2021_xpath = '//*[@id="years"]/option[2]'

    address_first_name_xpath = "//input[@id='firstname']"
    address_last_name_xpath = "//input[@id='lastname']"
    address_company_name_xpath = "//input[@id='company']"
    address_xpath = "//input[@id='address1']"
    address_city_xpath =  "//input[@id='city']"
    address_state_xpath = '//*[@id="id_state"]/option[2]'
    address_postcode_xpath = "//input[@id='postcode']"
    address_additional_info_xpath = '//*[@id="other"]'
    address_mobile_xpath = "//input[@id='phone_mobile']"

    register_button_xpath = "//span[normalize-space()='Register']"
    my_account_xpath = "//h1[normalize-space()='My account']"

    registered_email_xpath = "//input[@id='email']"
    registered_signin_button_xpath = "//span[normalize-space()='Sign in']"

    cart_dress_xpath = '//*[@id="block_top_menu"]/ul/li[2]/a'
    cart_dress_casual_xpath = "//a[@class='subcategory-name'][normalize-space()='Casual Dresses']"
    cart_printed_dress_xpath = '//*[@id="center_column"]/ul/li[1]/div/div[2]/h5/a'

    add_to_cart_xpath = "//span[normalize-space()='Add to cart']"
    proceed_to_checkout = "//span[normalize-space()='Proceed to checkout']"
    summary_proceed_to_click = "//a[@class='button btn btn-default standard-checkout button-medium']//span[contains(text(),'Proceed to checkout')]"
    summary_proceed_to_checkout = "//button[@name='processAddress']//span[contains(text(),'Proceed to checkout')]"
    summery_shipping_proceed_to_checkout = "//button[@name='processCarrier']//span[contains(text(),'Proceed to checkout')]"
