"""
algorithm thinking: week4

grid example:
cells = [ [... for col in range(grid_width)] for row in range(grid_height)]
"""


def build_scoring_matrix(alphabet, diag_score, off_diag_score, dash_score):
    """
    Takes as input a set of characters alphabet and three scores diag_score, off_diag_score, and dash_score.
    The function returns a dictionary of dictionaries whose entries are indexed by pairs of characters in alphabet plus '-'.
    The score for any entry indexed by one or more dashes is dash_score.
    The score for the remaining diagonal entries is diag_score.
    Finally, the score for the remaining off-diagonal entries is off_diag_score.
    """

    res = {}
    for let in alphabet:
        dct = {}
        res[let] = dct
        for let1 in alphabet:
            if let == let1:
                dct[let1] = diag_score
            else:
                dct[let1] = off_diag_score
            dct['-'] = dash_score
        
    dct = {}
    res['-'] = dct;
    for let in alphabet:
        dct[let] = dash_score;
        dct['-'] = None
    
    return res




def compute_alignment_matrix(seq_x, seq_y, scoring_matrix, global_flag):
    """
    Takes as input two sequences seq_x and seq_y whose elements share a common alphabet
    with the scoring matrix scoring_matrix. The function computes and returns the alignment matrix for seq_x and seq_y
    as described in the Homework.
    If global_flag is True, each entry of the alignment matrix is computed using
    the method described in Question 8 of the Homework. If global_flag is False, each entry is computed using the
    method described in Question 12 of the Homework.
    """

    return []


def compute_global_alignment(seq_x, seq_y, scoring_matrix, alignment_matrix):
    """
    Takes as input two sequences seq_x and seq_y whose elements share a common alphabet
    with the scoring matrix scoring_matrix.
    This function computes a global alignment of seq_x and seq_y using the global alignment matrix alignment_matrix.
    The function returns a tuple of the form (score, align_x, align_y)
    where score is the score of the global alignment align_x and align_y.
    Note that align_x and align_y should have the same length and may include the padding character '-'.
    """
    return (0, [], [])


def compute_local_alignment(seq_x, seq_y, scoring_matrix, alignment_matrix):
    """
    Takes as input two sequences seq_x and seq_y whose elements share a common alphabet
    with the scoring matrix scoring_matrix. This function computes a local alignment of seq_x and
    seq_y using the local alignment matrix alignment_matrix.
    The function returns a tuple of the form (score, align_x, align_y) where score is the score of
    the optimal local alignment align_x and align_y. Note that align_x and align_y should have
    the same length and may include the padding character '-'.
    """
    return (0, [], [])


