# SQLi

My Friend has created a website for his company. He has asked me to test it for any vulnerabilities. Can you help me out? I have a feeling that it is vulnerable to SQL Injection.

---

## Solution

From the hint/challenge description/challenge title, we know that the website is vulnerable to SQL Injection. We can exploit this vulnerability by entering a SQL query in the input field.

Entering `' OR '1'='1` in the input field will return the flag.

Flag: `YCEP24{SQL_1njec7i0n_15_fun}`
