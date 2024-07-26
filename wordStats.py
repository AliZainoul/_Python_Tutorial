import re
from typing import List, Tuple, Dict, Any

def filter_element(word: str) -> str:
    """
    Filters out specific punctuation characters from the word.
    
    Args:
        word (str): The word to be filtered.
        
    Returns:
        str: The filtered word with specified characters removed.
    """
    # Regex pattern for characters to remove
    reg = r"[+?&'()§!_-%¨`@#$€,;.:/=*]"
    # Filter out characters from the word using strip
    filtered_word = word.strip(reg)
    # TODO: replace with a good RegEx pattern!
    return filtered_word

def input_sentences() -> List[Tuple[str, ...]]:
    """
    Prompts the user to input sentences and processes them into a list of tuples of words.
    
    Returns:
        List[Tuple[str, ...]]: A list of sentences, each represented as a tuple of words.
    """
    number_of_sentences: int = int(input("Please enter the number of sentences: \n"))
    list_sentences: List[Tuple[str, ...]] = []
    
    for index in range(number_of_sentences):
        # Split the input sentence into words and filter each word
        tmp_l: List[str] = list(map(filter_element, input(f"Please enter sentence number {index + 1}: ").split()))
        tmp_t: Tuple[str, ...] = tuple(tmp_l)
        list_sentences.append(tmp_t)
    
    return list_sentences

def print_line() -> None:
    print("----" * 20)

def display_infos(container_: List[Tuple[str, ...]]) -> None:
    """
    Displays information about the container and its elements.
    
    Args:
        container_ (List[Tuple[str, ...]]): The container to display information about.
    """
    print_line()
    for element in container_:
        print(element)
        print(type(element))
        print_line()
        for elt in element:
            print(elt)
            print(type(elt))
        print_line()

def mean_sentences(sentences: List[Tuple[str, ...]]) -> float:
    """
    Calculates the average number of words per sentence.
    
    Args:
        sentences (List[Tuple[str, ...]]): The list of sentences.
        
    Returns:
        float: The average number of words per sentence.
    """
    total_words: int = sum(len(sentence) for sentence in sentences)
    average: float = total_words / len(sentences) if sentences else 0.0
    return average

def most_frequent_words(sentences: List[Tuple[str, ...]]) -> List[Tuple[str, int]]:
    """
    Determines the most frequent words in the given list of sentences.
    
    Args:
        sentences (List[Tuple[str, ...]]): The list of sentences.
        
    Returns:
        List[Tuple[str, int]]: A list of tuples containing words and their frequencies, sorted by frequency.
    """
    word_count: Dict[str, int] = {}
    
    for sentence in sentences:
        for word in sentence:
            # Increment the word count in the dictionary
            word_count[word] = word_count.get(word, 0) + 1
    
    # Sort the words by frequency in descending order
    sorted_word_count: List[Tuple[str, int]] = sorted(word_count.items(), key=lambda item: item[1], reverse=True)
    
    return sorted_word_count

# Example usage
result: List[Tuple[str, ...]] = input_sentences()

display_infos(result)
print(mean_sentences(result))
print(most_frequent_words(result))
