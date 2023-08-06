# -*- coding: utf-8 -*-
# pylint: disable=singleton-comparison
"""api.py"""
import contextlib
import cProfile
import io
import logging
import pstats
from typing import Optional

from spiderbot.models.base import BaseDB
from spiderbot.models.posts import Post
from spiderbot.models.posturls import PostURL
from spiderbot.models.users import User


@contextlib.contextmanager
def profiled():
    pr = cProfile.Profile()
    pr.enable()
    yield
    pr.disable()
    s = io.StringIO()
    ps = pstats.Stats(pr, stream=s).sort_stats('cumulative')
    ps.print_stats()
    # uncomment this to see who's calling what
    # ps.print_callers()
    print(s.getvalue())


logger = logging.getLogger(__name__)


class DBAPI(BaseDB):
    """the api of the database"""

    def add_user(self, user_url: str, working_status: Optional[bool] = None):
        """add new user to db"""
        with profiled():
            user = self.session.query(User).filter(User.user_url == user_url).first()
        if not user:
            self.add(
                User(
                    {
                        "user_url": user_url,
                        "working_status": working_status,
                    }
                )
            )
        return True

    def get_users_todo(self, working_status: Optional[bool] = None):
        """get the users url todo"""
        with profiled():
            users = self.session.query(User.user_url).filter(User.working_status == working_status).all()
        return users

    def get_users_to_get_profiles(self):
        """get the users url todo"""
        with profiled():
            users = (
            self.session.query(User.user_url)
            .filter(User.working_status == True)
            .filter(User.name == None)
            .all()
        )

        return users

    def update_user_profile(self, user_url: str, name: str, avatar: bytes):
        """update user profile"""
        _params = {}
        if name:
            _params["name"] = name
        if avatar:
            _params["avatar"] = avatar

        if _params:
            with profiled():
                self.session.query(User).filter(User.user_url == user_url).update(_params)
                self.commit()
                logger.info("update_user_profile %s", user_url)
        else:
            logger.info("update_user_profile %s no params", user_url)

    def add_post_url(self, user_url: str, post_url: str):
        """add post url to db"""
        with profiled():
            self.add(PostURL({"user_url": user_url, "post_url": post_url}))
        logger.info("add_post_url %s", post_url)

    def update_user_working_status(self, user_url: str, working_status: Optional[bool] = None):
        """update status of working"""
        with profiled():
            self.session.query(User).filter(User.user_url == user_url).update(
            {"working_status": working_status}
        )
            self.commit()
            logger.info("update_user_working_status %s", user_url)
        return True

    def update_url_content_status(self, post_url: str, content_status: bool):
        """update post_url content status"""
        with profiled():
            self.session.query(PostURL).filter(PostURL.post_url == post_url).update(
            {"content_status": content_status}
        )
            self.commit()
            logger.info("update_url_content_status %s", post_url)
        return True

    def get_posturls_to_getcontent(self):
        """get the urls which to get content"""
        with profiled():
            urls = self.session.query(PostURL.post_url).filter(PostURL.content_status == None).all()
        return urls 

    def add_post(self, post_url: str, post_time: str, text: str, screenshot: bytes):
        """add new post"""
        with profiled():
            self.add(
            Post(
                {
                    "post_url": post_url,
                    "text": text,
                    "screenshot": screenshot,
                    "post_time": post_time,
                }
            )
        )
            logger.info("add_post %s %s", post_url, post_time)
            self.update_url_content_status(post_url, True)
        return True

    def get_post(self, post_url: str):
        """get the post by post_url"""
        with profiled():
            post = self.session.query(Post).filter(Post.post_url == post_url).first()
            logger.info("get_post %s", post_url)
        return post

    def get_posts(self, uid=1):
        """get all posts data"""
        with profiled():
            posts = self.session.query(Post).filter(Post.uid >= uid).all()
            logger.info("get_posts")
        return posts

    def get_profiles(self, uid=1):
        """get all the profiles data"""
        with profiled():
            profiles = self.session.query(User).filter(User.uid >= uid).filter(User.name != None).all()
            logger.info("get_profiles")
        return profiles
