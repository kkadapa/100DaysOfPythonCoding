def main():
    book = 'Dracula'
    author = "Bram Stoker"

    print('Title:', book)
    print('Author:', author)

#  If you have an apostrophe within your sentence, you may want to use double quotes.
    question = "What's your name?"
    print(question)
# or the opposite
    sentence = 'Harriet Jacobs writes, "She sat down, quivering in every limb"'
    print(sentence)

# Triple quotes are a different case altogether. You can put multi-line strings within triple quotes and Python will preserve the white spaces as well.
    synopsis = """Dracula comprises journal entries, letters, and telegrams written by the main characters.
    It begins with Jonathan Harker, a young English lawyer, as he travels to Transylvania.
    Harker plans to meet with Count Dracula, a client of his firm, in order to finalize a property transaction.
    When he arrives in Transylvania, the locals react with terror after he discloses his destination: Castle Dracula.
    Though this unsettles him slightly, he continues onward.
    The ominous howling of wolves rings through the air as he arrives at the castle.
    When Harker meets Dracula, he acknowledges that the man is pale, gaunt, and strange.
    Harker becomes further concerned when, after Harker cuts himself while shaving, Dracula lunges at his throat.
    Soon after, Harker is seduced by three female vampires, from whom he barely escapes.
    He then learns Dracula’s secret—that he is a vampire and survives by drinking human blood.
    Harker correctly assumes that he is to be the count’s next victim.
    He attacks the count, but his efforts are unsuccessful.
    Dracula leaves Harker trapped in the castle and then, along with 50 boxes of dirt, departs for England."""

    print('Synopsis:', synopsis)

if __name__ == '__main__':
    main()
