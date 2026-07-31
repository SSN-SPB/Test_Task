import { HTTP_STATUS } from '../constants/httpStatus.js';
import { getAllUsers } from '../services/usersService.js';

/**
 * Handles GET /api/users requests.
 *
 * @param {import('express').Request} request Express request object.
 * @param {import('express').Response} response Express response object.
 */
export function getUsers(request, response) {
    const users = getAllUsers();

    response.status(HTTP_STATUS.OK).json(users);
}
