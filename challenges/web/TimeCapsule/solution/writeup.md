# Time Capsule

In this challenge, you are tasked with extracting a One-Time Password (OTP) hidden within the source code of the webpage, but that's just the first step. Adding this OTP into the input field will trigger a Timestamp error, which will notify you that the correct timestamp should be 100 years from today.

To solve the challenge, follow these steps:

Locate the OTP:

Inspect the source code of the webpage to find the hidden OTP. You can do this by right-clicking on the page and selecting View Source (or using Developer Tools).
Look for a comment, hidden field, or script that contains the OTP.
Understanding the Timestamp Requirement:

Once the OTP is entered, you will receive a Timestamp error, indicating that the timestamp should be exactly 100 years from today's date.
The timestamp needs to be in UNIX timestamp format, which represents the number of seconds since January 1, 1970 (UTC).
For example:

If the current date is March 20, 2025, the UNIX timestamp for that date would be 1742400000.
The correct timestamp for 100 years later, i.e., March 20, 2125, will be in the range 4898073600 to 4898159999 (inclusive).
The timestamp value should fall within this range to avoid the Timestamp error.
Modify the Timestamp:

Use a tool like Burp Suite Repeater to intercept and modify the request.
The key task is to modify the timestamp header in the request to the correct value.
Ensure that the timestamp corresponds to 100 years from today's date. This means replacing the incorrect timestamp sent with the original request with the value in the acceptable range.
Steps for Burp Suite Repeater:

Intercept the request: Use Burp Suite to capture the request that includes the OTP.
Modify the timestamp: Change the timestamp header to the correct value (within the acceptable range).
For example, if today is March 20, 2025, replace the timestamp with any value between 4898073600 and 4898159999.
Forward the request: Send the modified request back to the server. This should return a success message and reveal the flag.

Final Flag:
YCEP25{w3b_1n_1h3_fTR25743}