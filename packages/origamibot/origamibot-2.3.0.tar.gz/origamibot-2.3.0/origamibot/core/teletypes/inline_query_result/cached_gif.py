from ..base import InlineQueryResult, Field, InputMessageContent

from ..inline_keyboard_markup import InlineKeyboardMarkup


class InlineQueryResultCachedGif(InlineQueryResult):

    gif_file_id = Field()
    title = Field()
    caption = Field()
    parse_mode = Field()
    reply_markup = Field()
    input_message_content = Field()

    def __init__(self,
                 id: str,
                 gif_file_id: str,
                 title: str = None,
                 caption: str = None,
                 parse_mode: str = None,
                 reply_markup: InlineKeyboardMarkup = None,
                 input_message_content: InputMessageContent = None
                 ):
        super().__init__(id, 'gif')

        self.gif_file_id = \
            Field(gif_file_id, [str])

        self.title = \
            Field(title, [str])

        self.caption = \
            Field(caption, [str])

        self.parse_mode = \
            Field(parse_mode, [str])

        self.reply_markup = \
            Field(reply_markup, [InlineKeyboardMarkup])

        self.input_message_content = \
            Field(input_message_content, [InputMessageContent])