local tr = aegisub.gettext
scipt_name = tr"选择奇偶行"
script_description = tr"选择奇偶数行"


function sel_odd(subs, sel)
	local odd_number = {}
	local count = 0
	for i = 1, #subs do
		local l = subs[i]
		if l.section == '[Events]' then
			break
		end
		count = count + 1
	end

	for i = 1, #subs do
		local l = subs[i]
		if l.section == '[Events]' and (i-count)%2==1 then
			table.insert(odd_number, i)
		end
	end
	return odd_number
end

function sel_even(subs, sel)
	local odd_number = {}
	local count = 0
	for i = 1, #subs do
		local l = subs[i]
		if l.section == '[Events]' then
			break
		end
		count = count + 1
	end

	for i = 1, #subs do
		local l = subs[i]
		if l.section == '[Events]' and (i-count)%2==0 then
			table.insert(odd_number, i)
		end
	end
	return odd_number
end

aegisub.register_macro(scipt_name.."/选择奇数行", script_description, sel_odd)
aegisub.register_macro(scipt_name.."/选择偶数行", script_description, sel_even)