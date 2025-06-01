




## Known Issues

If a user enters a new admission result while scraping, this will result in a redundant entry on the next page scrapted, as the entries will shift down one. 

There are some blank lines in the grad cafe table, this has been handled in the simplest way, but may not be robust

Comments can have interesting anomolies like emojis and special symbols that come out weird in the JSON, handled with ```ensure_ascii=False```. Hopefully the downsides of this are minimal


## Reminders

Don't forget to clean up imports
Add metric printout at end of scraping (x sites in y seconds)