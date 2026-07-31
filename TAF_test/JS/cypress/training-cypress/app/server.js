import express from 'express';

import { APP_CONFIG } from './config/appConfig.js';
import { createUsersRouter } from './routes/usersRoutes.js';

const app = express();

app.use(express.json());

app.use(createUsersRouter());

app.get('/', (request, response) => {
    response.json({
        message: 'Training Cypress API is running',
    });
});

/**
 * Starts the Express application.
 *
 * @param {number} port Port used by the HTTP server.
 * @returns {import('http').Server} Running HTTP server.
 */
export function startServer(port = APP_CONFIG.port) {
    return app.listen(port, () => {
        console.log(`Server started on http://localhost:${port}`);
    });
}

startServer();
