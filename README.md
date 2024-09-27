# EWU Book Buy & Sell Testing

## 1. Introduction

**EWU Book Buy & Sell** is a web-based platform designed to facilitate the buying and selling of second-hand books within the **East West University** community. This project focuses on the testing strategies used to ensure the reliability, functionality, and security of the platform.

### 1.1 Purpose
The purpose of this project is to provide a detailed analysis of the testing methods employed to validate the performance and usability of the EWU Book Buy & Sell platform. It aims to identify potential issues and ensure that the software meets the highest standards of quality.

### 1.2 Scope
This document covers both static analysis and dynamic testing of the software, focusing on various test cases and their outcomes to guarantee that the platform functions as intended.

---

## 2. Key Features

### 2.1 Sequence Diagrams

1. **Sequence Diagram 1:** Overview of the system's main interaction flow.
2. **Sequence Diagram 2:** Detailed sequence diagram depicting the book buying process.
3. **Sequence Diagram 3:** Further sequences showcasing various user interactions with the platform.

### 2.2 LTSA Diagrams & Code

1. **Log In:**
   - Represents the process of user authentication, detailing user interactions, authentication checks, and system responses.

   ```plaintext
   USER = (provideData->clicklogin->(getloginAccepted->USER|getloginRejected->USER)).
   LogInPage = (getData->authData->(getUserAuth->loginAccepted->LogInPage|getAuthErr->loginejected->LogInPage)).
   Authentication = (getauthData->(userAuth->Authentication|authErr->Authentication)).
   ||LogIn = (USER || LogInPage || Authentication)/
   {authData/getauthData userAuth/getUserAuth authErr/getAuthErr provideData/getData loginAccepted/getloginAccepted loginejected/getloginRejected}.

2. **Book Buy:**
   - Represents the interaction process for buying books, including data provision, information retrieval, and display.
  
    ```plaintext
    USER = (provideBookData->(getInfo->USER|getNoInfo->USER)).
    BookStore = (getBookData->sendData->(info->getDisplayInfo->BookStore|noInfo->getNoDisplayInfo->BookStore)).
    Database = (rcvData->(displayInfo->Database|noDisplayInfo->Database)).
    ||BookBuy = (USER || BookStore || Database)/
    {provideBookData/getBookData getInfo/info getNoInfo/noInfo sendData/rcvData displayInfo/getDisplayInfo noDisplayInfo/getNoDisplayInfo}.

2. **Book Request:**
   - Details the request process for unavailable books, from form submission to data handling and display.

     ```plaintext
     USER = (reqBook->getForm->submitDetails->USER).
     BookReq = (getReqBook->sendFormReq->BookReq).
     Database = (sendForm->rcvFormReq->(displayBook->Database)).
     ||BookRequest = (USER || BookReq || Database)/
     {reqBook/getReqBook getForm/sendForm sendFormReq/rcvFormReq}.

---

## 3. Testing Strategy

### 3.1 Dynamic Testing

1. **Test Case 1: Log In**
   - Verifies the login functionality by testing various scenarios, including correct and incorrect email/password combinations, and validates user navigation upon successful login.
  
2. **Test Case 2: Request Book**
   - Evaluates the book request feature, ensuring proper handling of book request forms, data submission, and user feedback.

3. **Test Case 3: Search Book**
   - Tests the book search functionality, assessing the accuracy of search results based on different search queries and criteria.

---

## 4. Automation Testing
For automation testing, we utilize ***Selenium*** with test cases written in ***Python***. The website used for testing is the
**[EWU Book Buy & Sell website](https://github.com/abirkhan-zero/ewu-book-buy-sell-website)**. The **Chromium** WebDriver is employed to execute the tests.

### 4.1 Test Cases
**Log In:** 
 - Tests the login functionality with various scenarios including valid and invalid credentials.
 - Ensures correct navigation upon successful or unsuccessful login attempts.
   
**Search Test:**
 - Tests the search functionality of the platform.
   
**Book:**
 - Validates the book request feature.
   
**All Requests:**
 - Ensures proper handling and feedback for all book requests.

---

## 5. Conclusion
The EWU Book Buy & Sell web application is a valuable resource for the **EWU Community**, enabling efficient trading of second-hand academic materials. The testing strategy implemented in this project, including:

**Functional Testing:** Ensures the software's features like book listing, search, transaction processing, and user management operate effectively.

**Usability Testing:** Guarantees an intuitive user interface and smooth navigation.

**Security Testing:** Protects user data from unauthorized access and potential threats.

The comprehensive test cases, covering functional, usability, security, performance, and compatibility testing, confirm that the platform meets the highest standards of quality and reliability. Despite a few current limitations, further enhancements can significantly improve the platform's performance and user satisfaction.

---

## 6. Contributors
- Md. Abir Hasan Khan
- Adnan Rahman Tushar
- Humayun Rashid Rahat

**Submitted To:**

***Dr. Shamim H Ripon*** 

***Professor, Department of Computer Science & Engineering***

***East West University***

**Course:**
***CSE430 Software Testing and Quality Assurance***

---

## 7. Acknowledgements
Special thanks to **Dr. Shamim H Ripon** for his guidance and support throughout the project, and to the **East West University** community for their valuable feedback.

---

## 8. References
Sequence Diagrams

LTSA Code

Dynamic Testing

Functional Testing


