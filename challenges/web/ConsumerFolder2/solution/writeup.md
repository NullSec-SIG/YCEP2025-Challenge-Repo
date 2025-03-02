1. Click Search Records
2. Type "Chin Ray"
3. Click Admin Panel
4. Open DevTools and go to the Network tab
5. Refresh
6. Find a very suspicious "page.json" among the list
7. Find the entry that contains "true" instead of "false" in the 3rd argument
8. The first argument is your username. Decode the Base64 string in the second argument - this is your password
9. The derived credentials should be - username: radeon, password: never_miss_an_opportunity_to_miss_an_opportunity
10. Login
11. Profit