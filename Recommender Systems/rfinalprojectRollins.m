%class recommendation system, only for electives


%first, we need some info from the user
disp('Hello there.  Could you answer some questions so we can figure out which classes to recommend to you?')
grade = input('First, what is your grade level? ', 's');
disp('Out of the following topics, which are you interested in?')
disp('Science, Math, Art, Religion, College Prep, Theatre, Technology, Home Education.')
disp('please enter y or n for yes or no below.')
science = input('Science: ', 's');
math = input('Math: ', 's');
art = input('Art: ', 's');
religion = input('Religion: ', 's');
collegeprep = input('College Prep: ', 's');
theatre = input('Theatre: ', 's');
technology = input('Technology: ', 's');
homeeducation = input('Home Education: ', 's');
disp('Thank You.  We will now generate your recommendations.')
%add error checking later

%finally, we produce context aware recommendations
scienceKey = {'chemistry', 'biology'};
mathKey = {'algebra', 'calculus', 'pre-calculus'};
artKey = {'drawing', 'art'};
religionKey = {'bible'};
collegeKey = {'college'};
theatreKey = {'drama'};
technologyKey = {'computer', 'programming'};
homeKey = {'cooking'};

%lowercase all of the class names
n = size(ClassName);
for i = 1:n
    temp = ClassName(i,1);
    ClassName(i,1) = lower(temp);
end

%this finds the elective classes and adds them to a matrix called electives

for i = 1:n
        if GroupNumber(i) == 6
            electives(i,1) =ClassName(i,1);
        end
end


%begin finding science recommendation
if science == 'y'
    
    disp('')
    disp('Here are your science recommendations:')
    
    
   %pos has the position data for which classes have the given string
  for j = 1:size(scienceKey)
      for i = 1:n
          pos(i,1) = strfind(ClassName(i,1), scienceKey{1,j});
          if pos{i,1} >= 0
              disp(ClassName(i))
          end
      end
    
  end

end % end of science recommendations



%begin generate math recommendations

if math == 'y'
    
    disp('')
    disp('Here are your math recommendations:')
    
    
   %pos has the position data for which classes have the given string
  for j = 1:size(mathKey)
      for i = 1:n
          pos(i,1) = strfind(ClassName(i,1), mathKey{1,j});
          if pos{i,1} >= 0
              disp(ClassName(i))
          end
      end
    
  end

end % end of math recommendations




%begin finding art recommendation
if art == 'y'
    
    disp('')
    disp('Here are your science recommendations:')
    
    
   %pos has the position data for which classes have the given string
  for j = 1:size(artKey)
      for i = 1:n
          pos(i,1) = strfind(ClassName(i,1), artKey{1,j});
          if pos{i,1} >= 0
              disp(ClassName(i))
          end
      end
    
  end

end % end of art recommendations



%begin finding religion recommendation
if religion == 'y'
    
    disp('')
    disp('Here are your religion recommendations:')
    
    
   %pos has the position data for which classes have the given string
  for j = 1:size(religionKey)
      for i = 1:n
          pos(i,1) = strfind(ClassName(i,1), religionKey{1,j});
          if pos{i,1} >= 0
              disp(ClassName(i))
          end
      end
    
  end

end % end of religion recommendations


%begin finding college recommendation
if collegeprep == 'y'
    
    disp('')
    disp('Here are your college recommendations:')
    
    
   %pos has the position data for which classes have the given string
  for j = 1:size(collegeKey)
      for i = 1:n
          pos(i,1) = strfind(ClassName(i,1), collegeKey{1,j});
          if pos{i,1} >= 0
              disp(ClassName(i))
          end
      end
    
  end

end % end of college recommendations


%begin finding theatre recommendation
if theatre == 'y'
    
    disp('')
    disp('Here are your theatre recommendations:')
    
    
   %pos has the position data for which classes have the given string
  for j = 1:size(theatreKey)
      for i = 1:n
          pos(i,1) = strfind(ClassName(i,1), theatreKey{1,j});
          if pos{i,1} >= 0
              disp(ClassName(i))
          end
      end
    
  end

end % end of theatre recommendations



%begin finding science recommendation
if technology == 'y'
    
    disp('')
    disp('Here are your technology recommendations:')
    
    
   %pos has the position data for which classes have the given string
  for j = 1:size(technologyKey)
      for i = 1:n
          pos(i,1) = strfind(ClassName(i,1), technologyKey{1,j});
          if pos{i,1} >= 0
              disp(ClassName(i))
          end
      end
    
  end

end % end of technology recommendations


%begin finding science recommendation
if homeeducation == 'y'
    
    disp('')
    disp('Here are your home education recommendations:')
    
    
   %pos has the position data for which classes have the given string
  for j = 1:size(homeKey)
      for i = 1:n
          pos(i,1) = strfind(ClassName(i,1), homeKey{1,j});
          if pos{i,1} >= 0
              disp(ClassName(i))
          end
      end
    
  end

end % end of home ed recommendations

%{
disp(' ')
disp('Now, if you would like, we can do a custom recommendation.')
disp('Please enter the class keywords you would like us to use to generate')
disp(' enter "exit" to finish')
i = 1;
key = cell(1);
keywords = cell(15,1);
keepGoing = true;
while keepGoing == true
    
    key{1} = input('Type keyword or "exit" here: ', 's');
    if key{1} == 'exit'
        keepGoing = false;
    else
    keywords(i,1) = key{1};
    i = i + 1;
    end
    
end 

disp(' ')
disp('Now displaying classes with these keywords in their titles:')

for j = 1:size(keywords)
      for i = 1:n
          pos(i,1) = strfind(ClassName(i,1), keywords{1,j});
          if pos{i,1} >= 0
              disp(ClassName(i))
          end
      end
    
end


%}
