package APITestingUsingRestAssured;

import static io.restassured.RestAssured.given;
import static org.hamcrest.Matchers.*;

import org.testng.annotations.Test;

public class CreateUser {

    @Test
    void test_createUser() {

        given()
            .baseUri("https://reqres.in")
            .header("x-api-key", "reqres-free-v1")     // ✔ API key header
            .contentType("application/json")
            .body("{ \"name\": \"Priya\", \"job\": \"Tester\" }")
        .when()
            .post("/api/users")
        .then()
            //  verify 201
            .statusCode(201)

            //  verify name = Priya
            .body("name", equalTo("Priya"))

            .log().all();
    }
}
