# Problem Set 4A
# @author: Jw


def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    #Base case
    if len(sequence) == 1:
        return [sequence]

    permutations = []
    #Take out element that serves as first character
    for letter in sequence:
        remaining_letters = sequence.replace(letter, "")
        sublist_permutations = get_permutations(remaining_letters)  #permutations of sublist

        for i in sublist_permutations:
            permutations.append(letter + i)

    return permutations



if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    example_input = "job"
    print('Input:', example_input)
    print('Expected Output:', ['job', 'jbo', 'ojb', 'obj', 'bjo', 'boj'])
    print('Actual Output:', get_permutations(example_input))

    example_input1 = "a"
    print('Input:', example_input1)
    print('Expected Output:', ['a'])
    print('Actual Output:', get_permutations(example_input1))

    example_input2 = "be"
    print('Input:', example_input2)
    print('Expected Output:', ['be','eb'])
    print('Actual Output:', get_permutations(example_input2))


