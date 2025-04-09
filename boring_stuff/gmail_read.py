import ezgmail

# unreadThreads = ezgmail.unread()
# print(ezgmail.summary(unreadThreads))
# print(len(unreadThreads))
# print(str(unreadThreads[0]))
# print(unreadThreads[0].messages[0].subject)
# print(unreadThreads[0].messages[0].body)
# print(unreadThreads[0].messages[0].timestamp)
# print(unreadThreads[0].messages[0].sender)
# print(unreadThreads[0].messages[0].recipient)

# recentThreads = ezgmail.recent()
# print(len(recentThreads))

# resultThreads = ezgmail.search('test')
# resultThreads = ezgmail.search('label:UNREAD', 'from:ch_semen@mail.ru')
# resultThreads = ezgmail.search('label:UNREAD from:ch_semen@mail.ru')
# print(ezgmail.summary(resultThreads))

resultThreads = ezgmail.search('test attachment')
print(ezgmail.summary(resultThreads))
print(resultThreads[0].messages[0].attachments)
resultThreads[0].messages[0].downloadAttachment('myWifi.ino')
resultThreads[0].messages[0].downloadAllAttachments(downloadFolder='download')