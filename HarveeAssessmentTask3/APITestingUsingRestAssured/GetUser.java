package APITestingUsingRestAssured;

import static io.restassured.RestAssured.given;
import static org.hamcrest.Matchers.*;

import org.testng.annotations.Test;

public class GetUser {

    @Test
    void test_getUser() {

        given()
            .queryParam("page", 2)
        .when()
            .get("https://reqres.in/api/users")
        .then()
            // 1️. Status code validation
            .statusCode(200)

            // 2️. At least one user exists (data.size() > 0)
            .body("data.size()", greaterThan(0))

            .log().all();
    }
}
