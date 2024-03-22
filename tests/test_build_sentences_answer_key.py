import pytest
import json
from build_sentences import (get_seven_letter_word, parse_json_from_file, choose_sentence_structure,
                              get_pronoun, get_article, get_word, fix_agreement, build_sentence, structures)

def test_get_seven_letter_word(mocker):
    # Arrange
    mocker.patch("builtins.input", return_value="1234567")
    # Act
    result = get_seven_letter_word()    
    # Assert
    assert len(result) >= 7
    
    # Arrange
    mocker.patch("builtins.input", return_value="123456")
    with (pytest.raises(ValueError)):
        #Act/Assert
        result = get_seven_letter_word()
        

def test_parse_json_from_file(tmp_path):
    # Arrange
    test_data = '{"test":"test"}'
    file_path = tmp_path / "test.txt"
    with open(file_path, "w") as f:
        f.write(test_data)

    # Act
    result = parse_json_from_file(file_path)
    
    # Assert
    assert result["test"] == "test"
    
    # Arrange
    test_data = 'BAD DATA'
    file_path = tmp_path / "test.txt"
    with open(file_path, "w") as f:
        f.write(test_data)

    # Act/Assert
    with pytest.raises(json.JSONDecodeError):
        result = parse_json_from_file(file_path)
    
    # Arrange/Act/Assert
    with pytest.raises(FileNotFoundError):
        result = parse_json_from_file("nofilehere.txt")

def test_choose_sentence_structure():
    # Arrange/Act
    result = choose_sentence_structure()
    
    # Assert
    assert result in structures

def test_get_pronoun(mocker):
    # Arrange
    mocker.patch("random.choice", return_value="foo")
    # Act
    result = get_pronoun()
    # Assert
    assert result == "foo"

def test_get_article(mocker):
    # Arrange
    mocker.patch("random.choice", return_value="bar")
    # Act
    result = get_article()
    # Assert
    assert result == "bar"

def test_get_word():
    # Arrange
    words = ["alpha","beta","gamma"]
    # Act
    result = get_word('A', words)
    # Assert
    assert result == "alpha"

def test_fix_agreement(mocker):
    pass  

def test_build_sentence(mocker):
    # Arrange
    mocker.patch("build_sentences.get_article", return_value ="the")
    mocker.patch("build_sentences.get_pronoun", return_value ="he")
    data = {
        "adjectives":["clear"],
        "adverbs":["clearly"],
        "nouns":["rock"],
        "verbs":["see"],
        "prepositions":["against"]
    }
    structure = ["PRO","ADV","VERB","ART","ADJ","NOUN","PREP","ART","ADJ","NOUN"]
    seed_word="AAAAAAA"
    
    # Act    
    sentence = build_sentence(seed_word, structure, data)
    
    # Assert
    assert sentence == "He clearly sees the clear rock against the clear rock"