# Sample Postman Collection — JSONPlaceholder CRUD Tests
# Export this content by saving as a .json file and importing into Postman

# To import:
# 1. Open Postman
# 2. Click "Import" button
# 3. Choose the exported .json collection file

# ============================================================
# Requests to create manually in Postman:
# ============================================================

# --- FOLDER: GET Requests (Read) ---

# GET All Posts
# Method: GET
# URL: {{BASE_URL}}/posts
# Tests tab:
#   pm.test("Status 200", () => pm.response.to.have.status(200));
#   pm.test("Array not empty", () => pm.expect(pm.response.json()).to.be.an('array').that.is.not.empty);
#   pm.test("Response time < 1000ms", () => pm.expect(pm.response.responseTime).to.be.below(1000));

# GET Single Post
# Method: GET
# URL: {{BASE_URL}}/posts/1
# Tests tab:
#   pm.test("Status 200", () => pm.response.to.have.status(200));
#   pm.test("Has id field", () => pm.expect(pm.response.json()).to.have.property('id'));
#   pm.test("Has title field", () => pm.expect(pm.response.json()).to.have.property('title'));
#   pm.test("ID equals 1", () => pm.expect(pm.response.json().id).to.equal(1));

# GET Non-Existent Resource (404 test)
# Method: GET
# URL: {{BASE_URL}}/posts/99999
# Tests tab:
#   pm.test("Status 404", () => pm.response.to.have.status(404));

# --- FOLDER: POST Requests (Create) ---

# POST Create New Post
# Method: POST
# URL: {{BASE_URL}}/posts
# Body (raw JSON):
# {
#   "title": "Test Post Title",
#   "body": "This is test post body content",
#   "userId": 1
# }
# Tests tab:
#   pm.test("Status 201", () => pm.response.to.have.status(201));
#   pm.test("Response has id", () => pm.expect(pm.response.json()).to.have.property('id'));
#   pm.test("Title matches", () => pm.expect(pm.response.json().title).to.equal("Test Post Title"));
#   const newId = pm.response.json().id;
#   pm.environment.set("newPostId", newId);

# --- FOLDER: PUT/PATCH Requests (Update) ---

# PUT Update Post (full replace)
# Method: PUT
# URL: {{BASE_URL}}/posts/1
# Body (raw JSON):
# {
#   "id": 1,
#   "title": "Updated Title",
#   "body": "Updated body",
#   "userId": 1
# }
# Tests:
#   pm.test("Status 200", () => pm.response.to.have.status(200));
#   pm.test("Title updated", () => pm.expect(pm.response.json().title).to.equal("Updated Title"));

# --- FOLDER: DELETE Requests ---

# DELETE Post
# Method: DELETE
# URL: {{BASE_URL}}/posts/1
# Tests:
#   pm.test("Status 200", () => pm.response.to.have.status(200));

# --- FOLDER: Users ---

# GET All Users
# Method: GET
# URL: {{BASE_URL}}/users

# GET User by ID
# Method: GET
# URL: {{BASE_URL}}/users/1

# --- ENVIRONMENT SETUP ---
# Create a Postman Environment called "JSONPlaceholder"
# Variable: BASE_URL = https://jsonplaceholder.typicode.com

# ============================================================
# For ReqRes.in Authentication Tests:
# ============================================================

# POST Register User (ReqRes)
# Method: POST
# URL: https://reqres.in/api/register
# Body (raw JSON):
# {
#   "email": "eve.holt@reqres.in",
#   "password": "pistol"
# }
# Tests:
#   pm.test("Status 200", () => pm.response.to.have.status(200));
#   pm.test("Has token", () => pm.expect(pm.response.json()).to.have.property('token'));
#   pm.environment.set("AUTH_TOKEN", pm.response.json().token);

# POST Login (ReqRes)
# Method: POST
# URL: https://reqres.in/api/login
# Body (raw JSON):
# {
#   "email": "eve.holt@reqres.in",
#   "password": "cityslicka"
# }
# Tests:
#   pm.test("Status 200", () => pm.response.to.have.status(200));
#   pm.test("Has token", () => pm.expect(pm.response.json()).to.have.property('token'));
#   pm.environment.set("AUTH_TOKEN", pm.response.json().token);

# POST Login — Wrong Password (Error scenario)
# Method: POST
# URL: https://reqres.in/api/login
# Body (raw JSON):
# {
#   "email": "eve.holt@reqres.in",
#   "password": "wrongpassword"
# }
# Tests:
#   pm.test("Status 400", () => pm.response.to.have.status(400));
#   pm.test("Has error message", () => pm.expect(pm.response.json()).to.have.property('error'));

# POST Register — Missing Password (Error scenario)
# Method: POST
# URL: https://reqres.in/api/register
# Body (raw JSON):
# {
#   "email": "test@reqres.in"
# }
# Tests:
#   pm.test("Status 400", () => pm.response.to.have.status(400));
#   pm.test("Error mentions missing password", () => {
#     pm.expect(pm.response.json().error).to.include('password');
#   });
