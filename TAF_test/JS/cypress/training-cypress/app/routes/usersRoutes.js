import { Router } from 'express';

import { API_ROUTES } from '../constants/apiRoutes.js';
import { getUsers } from '../controllers/usersController.js';

const usersRouter = Router();

/**
 * Registers the users API route.
 *
 * @returns {import('express').Router} Configured users router.
 */
export function createUsersRouter() {
    usersRouter.get(API_ROUTES.USERS, getUsers);

    return usersRouter;
}
