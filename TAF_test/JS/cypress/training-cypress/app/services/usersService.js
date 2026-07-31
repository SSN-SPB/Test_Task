import users from '../data/users.json' with { type: 'json' };

/**
 * Retrieves all users.
 *
 * @returns {Array<Object>} List of users.
 */
export function getAllUsers() {
    return users;
}
