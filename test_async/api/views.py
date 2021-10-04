from aiohttp import web


class TodoViewList(web.View):
    async def get(self):
        """
        ---
        description: This end-point allow to test that service is up.
        tags:
        - TODO
        produces:
        - text/plain
        responses:
            "200":
                description: successful operation. Return Todo object
            "405":
                description: invalid HTTP Method
        """
        connection = self.request.app['db_connection']
        async with connection.acquire() as conn:
            curr = await conn.cursor()
            await curr.execute("SELECT * FROM todos")
            todos = await curr.fetchall()
            print(todos)
            return web.Response(text=str(todos))

    async def post(self):
        """
        ---
        description: This end-point allow to test that service is up.
        tags:
        - TODO
        produces:
        - text/plain
        parameters:
        - in: body
          name: body
          description: Created todo object
          required: true
          schema:
            type: object
            properties:
                title:
                    type: string
                text:
                    type: string
        responses:
            "200":
                description: successful operation. Created todo object
            "405":
                description: invalid HTTP Method
        """
        connection = self.request.app['db_connection']
        async with connection.acquire() as conn:
            data = await self.request.json()
            curr = await conn.cursor()
            await curr.execute(f"INSERT INTO todos(title, text) VALUES ('{data['title']}','{data['text']}')")
            return web.Response()


class TodoViewSingle(web.View):
    async def get(self):
        """
        ---
        description: This end-point allow to test that service is up.
        tags:
        - TODO
        produces:
        - text/plain
        parameters:
        - in: path
          name: id
          type: integer
          format: int64
          description: todo id
          required: true
        responses:
            "200":
                description: successful operation. Return todo object
            "405":
                description: invalid HTTP Method
        """
        connection = self.request.app['db_connection']
        async with connection.acquire() as conn:
            id = self.request.match_info.get('id', None)
            if not id:
                return web.Response(text="Todo not found")
            id = int(id)
            curr = await conn.cursor()
            await curr.execute(f"SELECT * FROM todos WHERE todo_id = {id}")
            todo = await curr.fetchone()
            print(todo)
        if todo:
            return web.Response(text=str(todo))
        return web.Response(text="Todo not found")

    async def put(self):
        """
        ---
        description: This end-point allow to test that service is up.
        tags:
        - TODO
        produces:
        - text/plain
        parameters:
        - in: path
          name: id
          type: integer
          format: int64
          description: todo id
          required: true
        - in: body
          name: body
          description: Updated todo object
          required: true
          schema:
            type: object
            properties:
                title:
                    type: string
                text:
                    type: string
        responses:
            "200":
                description: successful operation. Updated Todo object
            "405":
                description: invalid HTTP Method
        """
        connection = self.request.app['db_connection']
        async with connection.acquire() as conn:
            id = self.request.match_info.get('id', None)
            if not id:
                return web.Response(text="Todo not found")
            id = int(id)
            data = await self.request.json()
            curr = await conn.cursor()
            await curr.execute(f"UPDATE todos SET title = '{data['title']}', text = '{data['text']}' WHERE todo_id = {id}")
        return web.Response()

    async def delete(self):
        """
        ---
        description: This end-point allow to test that service is up.
        tags:
        - TODO
        produces:
        - text/plain
        parameters:
        - in: path
          name: id
          type: integer
          format: int64
          description: todo id
          required: true
        responses:
            "200":
                description: successful operation. Return todo object
            "405":
                description: invalid HTTP Method
        """
        connection = self.request.app['db_connection']
        async with connection.acquire() as conn:
            id = self.request.match_info.get('id', None)
            if not id:
                return web.Response(text="Todo not found")
            id = int(id)
            curr = await conn.cursor()
            await curr.execute(f"DELETE FROM todos WHERE todo_id = {id}")
        return web.Response()
