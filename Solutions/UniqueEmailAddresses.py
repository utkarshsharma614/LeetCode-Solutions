class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        a = set()
        for email in emails:
            local, domain = email.split('@')
            if '+' in local:
                local = local[:local.index('+')]
            a.add(local.replace('.', '') + '@' + domain)
        
        return len(a)