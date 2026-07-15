class Solution:
    def isPalindrome(self, s: str) -> bool:
        def remove_non_alphanumeric_isalnum(input_string):
            # This generates an iterable of only alphanumeric characters
            alphanumeric_chars = (c for c in input_string if c.isalnum())
            # This joins the characters in the iterable into a new string
            cleaned_string = "".join(alphanumeric_chars)
            return cleaned_string.lower()
        s=remove_non_alphanumeric_isalnum(s)
        return True if s==s[::-1] else False
        

        