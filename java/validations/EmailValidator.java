import java.util.regex.Pattern;

public class EmailValidator {
	public static Boolean validate(String email) {
		String regex = "^(?:[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.(?:com|com\\.[a-z]{2,3}))$";
		return Pattern.matches(regex, email);
	}
}
