# Goal (Requirement)

Allow registered users to reset a forgotten password without contacting support.

# Background (Requirement)

The application currently supports password changes only for authenticated
users. A signed-out user who forgets a password cannot recover the account.

The reset flow must avoid revealing whether an email address is registered.

# Implementation (Design)

Add a password-reset request flow and a token-based password-update flow. Both
known and unknown email addresses receive the same public response. Only known
accounts receive reset email.

Reset tokens are single-use, expire after 30 minutes, and are stored as hashes.

## Details

- Add an endpoint that accepts an email address and requests a password reset.
- Generate and persist a hashed reset token for a registered account.
- Send the raw token to the account email in a reset link.
- Add an endpoint that accepts the token and new password.
- Validate the token, update the password hash, and consume the token atomically.

## Order

1. Add token persistence and expiration handling.
2. Add password-reset request behavior.
3. Add password-update behavior.
4. Add the signed-out reset UI.
5. Add the required tests.

## Constraints

- Return the same reset-request response for known and unknown email addresses.
- Never persist or log a raw reset token.
- Consume a valid token in the same transaction as the password update.
- Preserve the existing authenticated password-change flow.

## Out of Scope

- Changing the password-strength policy.
- Adding account recovery methods other than email.
- Revoking existing sessions after a password reset.

# Verification

## E2E Tests — Critical User Journeys Only

### Update

None — existing E2E tests do not cover signed-out password recovery.

### New

#### Scenario: Reset a forgotten password

- GIVEN a registered user is signed out
- WHEN the user requests a reset and submits a valid new password from the email link
- THEN the user can sign in with the new password
- AND the old password no longer works

#### Scenario: Open an expired reset link

- GIVEN a registered user has an expired reset link
- WHEN the user submits a new password from that link
- THEN the user sees that the link is invalid or expired
- AND the password is not changed

## Integration Tests

### Update

- `tests/auth/password_reset_test.go::request_reset` — expect the same public response for known and unknown email addresses
- `tests/auth/password_change_test.go::change_password` — add regression coverage for the existing authenticated password-change flow

### New

- registered account requests a password reset -> hashed token is persisted and reset email is queued
- unknown email requests a password reset -> successful public response with no token or email created
- valid token and valid new password are submitted -> password is updated and token is consumed
- expired token and valid new password are submitted -> expiration error and unchanged password
- previously consumed token is submitted again -> invalid-token error and unchanged password
- password persistence fails after a valid token is submitted -> password and token remain unchanged
- password reset is requested -> application logs do not contain the raw reset token

## Unit Tests

### Update

None — existing unit-test expectations remain valid.

### New

- reset token created 29 minutes and 59 seconds ago -> valid token data
- reset token created 30 minutes ago -> `ErrResetTokenExpired`
- malformed reset token -> `ErrInvalidResetToken`
- password shorter than the configured minimum -> `ErrPasswordTooShort`

# Done When

- A registered signed-out user can reset a forgotten password through email.
- Password-reset requests do not reveal whether an account exists.
- Reset tokens expire after 30 minutes and cannot be reused.
- Raw reset tokens are not persisted or logged.
- The existing authenticated password-change flow continues to work.
- All listed verification cases pass.
