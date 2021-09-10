#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# @File     : Redis.py
# @Time     : 2021/9/6 19:41
# @Author   : NagisaCo
import asyncio_redis


class Redis(object):
    def __init__(self, host: str = 'localhost', password: str = None, port: int = 6379, db: int = 2):
        self.host = host
        if password is None:
            self.password = None
        else:
            self.password = password.encode(encoding='utf-8')
        self.port = port
        self.db = db
        self.pool = None

    async def connect(self):
        self.pool = await asyncio_redis.Pool.create(
                host=self.host,
                password=self.password,
                port=self.port,
                db=self.db,
                poolsize=20
            )
        print("redis connected")

    async def disconnect(self):
        self.pool.close()
