# Testdata

## Deployment

To use the project, you have to do the following steps:

    cd <project_folder>
    git clone https://github.com/kecks2010/testdata.git
    cd testdata
    git status

You should get the following output:

    On branch mater
    Your branch is up to date with 'origin/master'.

    nothing to commit, working tree clean

And now, you have to install the project to your local python environment.

    poetry install
    poetry build

## ID card validator and generator
In most cases, providing personal data is completely sufficient. However, there are also use cases where personal data
must be validated. One type of validation is to compare the entered data with the data on the identity card or passport.
To do this, however, it is necessary to check the identity card or passport itself to ensure that it is a real identity
card or passport. This means that the data must be checked for consistency:

- Does the document number match the type of ID?
- Are the document number, date of birth, and expiry date the correct length?
- Are the checksums of the respective fields correct?
- Does the overall checksum match?
- Is the ID still valid or already expired?
- ...

Checking the ID data is one point. The far more important point for the test is to get access to precisely such data.
Because testing with real ID data is not only difficult, but also involves strict requirements due to the General Data
Protection Regulation. So instead of working with real ID data, it is better to generate corresponding ID data in the
test.

### Old identity card

| Field           | Structure and format                 |
|-----------------|--------------------------------------|
| Document number | 9 digits plus 1 check digit          | 
| Birth date      | 6 digits (yymmdd) plus 1 check digit |
| Expiry date     | 6 digits (yymmdd) plus 1 check digit |
| Check digit     | Check digit over all                 | 

### New identity card without version

| Field           | Structure and format                 |
|-----------------|--------------------------------------|
| Document number | 9 characters and 1 check digit       | 
| Birth date      | 6 digits (yymmdd) plus 1 check digit |
| Expiry date     | 6 digits (yymmdd) plus 1 check digit |
| Check digit     | Check digit over all                 | 

**Document number**\
First character - one of L, M, N, P, R, T, V, W, X, Y\
Allowed characters - 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, C, F, G, H, J, K, L, M, N, P, R, T, V, W, X, Y, Z\
Not allowed characters - A, E, I, O, U, B, D, Q, S

### New identity card with version

| Field           | Structure and format                 |
|-----------------|--------------------------------------|
| Document number | 9 characters and 1 check digit       | 
| Birth date      | 6 digits (yymmdd) plus 1 check digit |
| Expiry date     | 6 digits (yymmdd) plus 1 check digit |
| Version         | yymm                                 |
| Check digit     | Check digit over all                 | 

**Document number**\
First character - one of L, M, N, P, R, T, V, W, X, Y\
Allowed characters - 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, C, F, G, H, J, K, L, M, N, P, R, T, V, W, X, Y, Z\
Not allowed characters - A, E, I, O, U, B, D, Q, S

### Passport

| Field           | Structure and format                 |
|-----------------|--------------------------------------|
| Document number | 9 characters and 1 check digit       | 
| Birth date      | 6 digits (yymmdd) plus 1 check digit |
| Expiry date     | 6 digits (yymmdd) plus 1 check digit |
| Version         | yymm<<<<<<<<<< plus 1 check digit    |
| Check digit     | Check digit over all                 | 

**Document number**\
First character - one of C, F, G, H, J, K\
Allowed characters - 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, C, F, G, H, J, K, L, M, N, P, R, T, V, W, X, Y, Z\
Not allowed characters - A, E, I, O, U, B, D, Q, S

### Temporary Passport

| Field           | Structure and format                 |
|-----------------|--------------------------------------|
| Document number | 9 characters and 1 check digit       | 
| Birth date      | 6 digits (yymmdd) plus 1 check digit |
| Expiry date     | 6 digits (yymmdd) plus 1 check digit |
| Check digit     | Check digit over all                 | 

**Document number**\
First character - one of A, B\
Second character - &lt;\
Allowed characters - 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, C, F, G, H, J, K, L, M, N, P, R, T, V, W, X, Y, Z\
Not allowed characters - A, E, I, O, U, B, D, Q, S

### Children Passport

| Field           | Structure and format                 |
|-----------------|--------------------------------------|
| Document number | 9 characters and 1 check digit       | 
| Birth date      | 6 digits (yymmdd) plus 1 check digit |
| Expiry date     | 6 digits (yymmdd) plus 1 check digit |
| Check digit     | Check digit over all                 | 

**Document number**\
First character - one of  E, F, G\
Second character - &lt;\
Allowed characters - 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, C, F, G, H, J, K, L, M, N, P, R, T, V, W, X, Y, Z\
Not allowed characters - A, E, I, O, U, B, D, Q, S