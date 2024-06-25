6/20/24 - verify script function with test server instead of live view
6/22/24 - need to figure out redirect issue. belive is has something to do with params not being saved to local storage before redirect
6/24/24 - more auth work - log in works if you enter the dev server in URL search directly, but not from django link. fuck if i know why
6/24/24 - figured out AUTH issue. JFC that was annoying. RedirectURI MUST match Django server address in order to work. localhost != 127.0.0.1